
Attachment between the rollers and the deformable surface
=======================
### Introduction

To fabricate the gripper, the deformable surface is fixed on the two actuated rollers (see [Fabrication](fabrication.md)).
We provide two ways of simulating this attachement of the deformable surface on the rollers.
The first way is to place springs between some nodes of the deformable surface and some rigid point that we will place on the rollers. 
The second way is to fuse the degrees of freedom of the rollers and the deformable surface.


### Attachement with springs
At the creation of the simulation scene, we will create the springs between the mesh and the roller, to simulate a kind of "glue". 
In the creation of the scene, we take the positions of the nodes of the mesh

```python
   numNodes = len(position)
   for p in range(numNodes):
            x = position[p][0];
            y = position[p][1];
            z = position[p][2];
```



            
