Fabricating, Simulating and Controlling the W-Gripper
=======================
Contributors: Zhongkai Zhang, Piyush Jain, Erwan Douaille, Jeremie Dequidt, Christian Duriez

### Introduction

This tutorial is about modeling, simulating and fabricating an original soft gripper called __WGripper__ in Sofa-SR.

The WGripper has to grasp any small phsysical object such has pens or lighters. Objects will be grasped by a rubber band attached on two cylinders. Those cylinders will be rotated by two actuators, the rotation will stretch or compress the rubber band. During the compression, the object will be stuck by the gripper in the gap between the two cylinders.

The simulation aspects is done using Sofa-SR. Sofa-SR is a modeling, simulation and control environment for Soft-Robotics using Sofa a real-time simulation framework for rigid and deformable mechanics. Sofa-SR is available from https://project.inria.fr/softrobot/

This tutorials is strongly inspired from https://softroboticstoolkit.com/book/pneunets-bending-actuator, the biggest difference is on how to use the Sofa+Soft-Robot for modeling and simulation and control. 

#### Prerequisites
To follow this tutorial you need a working version of Sofa. We provide a Linux disk image with a pre-compiled version of Sofa with all the material for this tutorials. 

Otherwise you need to get sofa & its soft-robotic toolkit plugin:
- Sofa (from http://www.sofa-framework.org)
- Soft-Robotic plugin (from https://project.inria.fr/softrobot/)

#### This Tutorials is composed of: 
- [Modeling](docs/modeling.md)
- [Simulation](docs/simulation.md)
- [Fabrication](docs/fabrication.md)
- [Control](docs/control.md)
