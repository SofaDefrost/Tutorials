Simulating
=======================
### Introduction

The simulation is done using the SOFA Open Source Framework and the "Soft-Robots" Plugin  dedicated for Real-time simulation of Soft Robots. To define the simulation, a Python scene file is created and fed as input to SOFA. In the following, we will describe, step by step, the creation of scene file that perfrom the simulation of the soft W-Gripper. 

#### This Tutorials is composed of: 
- [Step 1 : Environment](simulationEnvironment.md)
- [Step 2 : Rollers](simulationRollers.md)
- [Step 3 : FEM W mesh](simulationFEMWMesh.md)
- [Step 4 : Attachment](simulationAttachment.md)
- [Step 5 : Collision](simulationCollision.md)

#### Basis of the scene

Let's define the basis of the scene as shown below : 

```python
import Sofa
import math
import os
path = os.path.dirname(os.path.abspath(__file__))+'/mesh/'
meshrobot=path+'finger0.vtu'

from math import cos, sin 

cylinderOffset = 30.0;
Radius=22.75

graspedObjectRadius=13;
graspedObjectHeight=40;
mass=0.01;


R=graspedObjectRadius;
h=graspedObjectHeight;

volume = R*R*3.14*h

def transformTableInString(Table):
        sizeT =  len(Table);
        strOut= ' ';
        for p in range(sizeT):
            strOut = strOut+ str(Table[p])+' '

        return strOut


def createScene(rootNode):
        rootNode.findData('gravity').value='-981.0 0 0';
        rootNode.findData('dt').value="0.01"
        rootNode.createObject('RequiredPlugin', pluginName='SoftRobots')
        rootNode.createObject('VisualStyle', displayFlags='showVisualModels hideBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')
        rootNode.createObject('BackgroundSetting', color='0 0.168627 0.211765')
        rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")


        ###################################################################
        # Direct simulation
        ###################################################################
        rootNode.createObject('FreeMotionAnimationLoop')
        rootNode.createObject('GenericConstraintSolver', printLog='0', tolerance="1e-15", maxIterations="10000")
        rootNode.createObject('CollisionPipeline', verbose="0")
        rootNode.createObject('BruteForceDetection', name="N2")
        rootNode.createObject('RuleBasedContactManager', name="Response", response="FrictionContact", rules="0 * FrictionContact?mu=0.8" )
        rootNode.createObject('LocalMinDistance', name="Proximity", alarmDistance="3", contactDistance="1", angleCone="0.01")

        ###################################################################
        # Control of the robot with the keyboard
        ###################################################################
        rootNode.createObject('PythonScriptController', filename="controllerGripper.py", classname="controller")
```

  Some recurring parameters have been stored in variables such as *cylinderOffset* or its *radius* so that simulations can be run easily by changing only the value of these parameters.
  
  It has been chosen that all the distances would be displayed in millimeters. Therefore, the gravity value is specified in kg.mm.s^-2 and has been voluntarily lowered ten times compared to the actual gravity for the needs of the simulation. Moreover, the chosen vertical axis is the X-axis ; then, the gravity worthes -981.0 along the X-axis.
  
  The direct simulation paragraph is composed by some solvers required to do some heavy computations during animations. The computation time is very long beacause the gripper - called *finger0.vtu* - contains many nodes in contact either with the grasped object or the two cylinders that make it rotate. These many interactions are the reason of difficulties in computing quickly.
  
  The *controllerGripper.py* file consists in a separate file responsible for managing the control during the simulation. For instance, the  pressing of the "CTRL" key simultaneously with the up or down arrow on the keyboard allows the cylinders to go up or down in the simulation. The same principle is to press "CTRL" with the "+" or "-" key in order to make the cylinders rotate clockwise or counter-clockwise with different speeds according to the number of times the "+" or the "-" key is pressed. These commands are necessary to the grasping of the object, the protocol is the following one : 
  
  1. First, the operator lower the mechanism ; the cylinders force the gripper to go downside towards the fixed floor aon which the object to grasp is laying.
  2.
  3.
  
