
# Step 1 : Environment

As a first step, we need to define the simulation environment. What we need is a flat floor and an object which will be grasped by our gripper.

![Environment](../images/WGripper_Simulation_Environment.png)

Let's create our floor function:
```python
        ################################ Fix Floor ################################
  def createFloor(node):
        floorNode = node.createChild('Floor') ## create a new graph node dedicated to the floor
        floorNode.createObject('MeshObjLoader', name='loader', filename="mesh/floorFlat.obj", rotation="0 0 270", scale =5, translation="30 0 0") ## Mesh Obj loader will load the floorFlat.obj file and then we rotate/translate/scale 
        floorNode.createObject('Mesh', src="@loader") ## Mesh is loaded using the MeshObjLoader reference @loader
        floorNode.createObject('MechanicalObject', src="@loader") ## store the degrees of freedom of each nodes of the mesh
        floorNode.createObject('Triangle',simulated="0", moving="0") ## collision model will react with triangles
        floorNode.createObject('Line',simulated="0", moving="0") ## collision model will react with lines
        floorNode.createObject('Point',simulated="0", moving="0") ## collision model will react with points
        floorNode.createObject('OglModel',name="Visual", fileMesh="mesh/floorFlat.obj", color="1 0 0 1",rotation="0 0 270", scale =5, translation="30 0 0") ## The visual part using the floorFlat.obj available by default in sofa/share/mesh
        return floorNode
```
The floor will be collision responsive using triangle/line/points object. We simply create a mechanical object then attach a mesh on it. Now we have to create the floor by calling the function from the createScene function.

```python
        floorNode = createFloor(rootNode)
```

Then the grasped object. This one will be more complicated because it will interract with the rubber band. 
```python
################################ Grasped Object ###################################
def createGraspedObject(node):
        # mechanics
        graspedNode =node.createChild('graspedNode') ## create a new graph node for our grasped object
        graspedNode.createObject('EulerImplicit', name='odesolver')
        graspedNode.createObject('CGLinearSolver', name='graspedNodeSolver', iterations='25', tolerance='1e-05', threshold='1e-05')
        graspedNode.createObject('MechanicalObject', template="Rigid", scale="1", position='38 0 0 0 0 0 1')

        ## Compute and apply 3d inertia tensors for a cylinder (aka our graspedObject)
        Ix= mass/12.0*(3.0*R*R + h*h)
        Iy= mass/12.0*(3.0*R*R + h*h)
        Iz= mass*R*R/2.0
        graspedNode.createObject('UniformMass', mass='0.01'+str(volume)+' ' +str(Ix)+ ' 0 0 0 '+str(Ix)+' 0 0 0 '+str(Iz))
        graspedNode.createObject('UncoupledConstraintCorrection')

        #collision parts 
        graspedNodeCollis = graspedNode.createChild('graspedNodeCollis')
        graspedNodeCollis.findData('activated').value=1
        graspedNodeCollis.createObject('MeshObjLoader', name="loader", filename="mesh/cylinder_JD.obj", triangulate="true",  scale3d="300 300 2000", translation="0 0 -20") 
        graspedNodeCollis.createObject('Mesh', src="@loader") 
        graspedNodeCollis.createObject('MechanicalObject') 
        graspedNodeCollis.createObject('Triangle') 
        graspedNodeCollis.createObject('Line') 
        graspedNodeCollis.createObject('Point') 
        graspedNodeCollis.createObject('RigidMapping')

        #visualization, simply create a dedicated visual node inside our current node and use a mesh described by cylinder_JD.obj. Map mesh points to the mechanical object using RigidMapping
        graspedNodeVisu = graspedNode.createChild('graspedNodeVisu')
        graspedNodeVisu.createObject('OglModel', name="Visual", fileMesh="mesh/cylinder_JD.obj", color="0.0 0.1 0.5", scale3d="300 300 2000" , translation="0 0 -20")
        graspedNodeVisu.createObject('RigidMapping')
        return graspedNode
```

And add it to the createScene function : 

```python
        graspedObjectNode = createGraspedObject(rootNode)
```
Congratulation ! We have the basics of the simulation. Continue to the step 2 : [Rollers](simulationRollers.md) 
