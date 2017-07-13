# Modeling

## Basic Concept

## 3D Model

Since the geometry of the gripper is simple, modeling the gripper in any of CAD / Modeling software is quite straight-forward: first you have to design a planar shape and then to extrude it along the Y-axis. Even if it is possible to mesh it with triangles, we recommend to use quads because it will enable to automatically build hexahedra for the FEM simulation.

![Surface Mesh](../images/WGripper_Surface_Mesh.png)

![Surface Mesh with Quads](../images/WGripper_Surface_Mesh_Rendered.png.png)

## Volumetric Mesh 

Starting from the 3D model (surface mesh), it is mandatory to compute volume elements for the FEM simulation. Standard volume elements are tetrahedral elements or hexahedral elements. SOFA provides some tools to ease the creation of the volumetric mesh given a surface model.

### with Tetrahedra

### with Hexahedra

![Hexahedral Mesh](../images/WGripper_Volume_Mesh_hexa.png)