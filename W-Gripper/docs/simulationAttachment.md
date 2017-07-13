
Attachment between the rollers and the deformable surface
=======================
### Introduction

To fabricate the gripper, the deformable surface is fixed on the two actuated rollers (see [Fabrication](fabrication.md)).
We provide two ways of simulating this attachement of the deformable surface on the rollers.
The first way is to place springs between some nodes of the deformable surface and some rigid point that we will place on the rollers. 
The second way is to fuse the degrees of freedom of the rollers and the deformable surface.


### Method 1: Attachement with springs
At the creation of the simulation scene, we will create the springs between the mesh and the roller, to simulate a kind of "glue". 
![Attach_concept](../images/Attach_1.tiff)
   
#### Python code
In the creation of the scene, we take the positions of the nodes of the mesh. We detect the nodes of the mesh that are placed on the part where we want to attach the nodes. Then, we fill two lists:
* mapPos that contains the position of the attachement in the local frame of the Roller
* indices which contains the indices of the attached nodes

The following code allows to fill these two lists for the left rollers
```python
   mapPos=[];
   indices=[];
   numNodes = len(position)
   eps=0.000001 #small value
   for p in range(numNodes):
            x = position[p][0];
            y = position[p][1];
            z = position[p][2];
            if (y+eps>H) & (x - L/2 < -D/2):
                
                l = L/2- D/2  - x; 
                theta = l / R;
                mapPos = mapPos + [-R*sin(teta), R*cos(teta), z] #be carreful of possible initial rotation of the rollers
                indices = indices + [p];
```

![Attach_concept](../images/Attach_2.tiff)

Then, we will use these two lists to create:
* the attachement points on the roller (we use the RigidMapping)
```python
        cylinderAttachPoints = cylinder.createChild('cylinderAttachPoints')
        cylinderAttachPoints.createObject('MechanicalObject', name='attachPointsMO', position = transformTableInString(mapPos))
        cylinderAttachPoints.createObject('RigidMapping')
```

* the springs (we use the RestShapeSpringsForceField and we inform the component that the "rest position" is provided by the points we just created. Moreover, the list of indices that was computed below is set in the data "points".
```python
        rubber.createObject('RestShapeSpringsForceField', points=transformTableInString(indices), stiffness='1000', external_rest_shape='../cylinder/cylinderAttachPoints/attachPointsMO')
```

#### Results
![Video](../videos/attachement.mov)

#### Advantage
This method is quite simple to implement and does not create much additional computation costs

#### Drawback
The drawback of this method, and in particular the "RestShapeSpringsForceField", is the fact that the spring force is only applied to the mesh, and not on the rollers. In fact the roller motion is still computed separately, as if it was a separated mechanical component. It becomes, somehow a "master" and the deformable surface becomes the "slave".



            
