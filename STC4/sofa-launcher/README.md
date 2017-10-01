Sofa-launcher
===========
Sofa-launcher is a simple API and tool to start multiple independent variation of a single Sofa scene. The different run can be executed in sequence, in parallel on multiple CPU or distributed on different computer. 

Disclaimer: 
This tutorial has been specifically made for the STC4 (2017/10/05) and may now be outdate.
Please consult the maintened sofa-launcher documentation at
http://www.github.com/sofa-framework/sofa/tools/sofa-launcher/README.md

# Write and test the scene to simulate
Sofa-launcher is independent on the langage you are using to write scene. You can write your scene in any langage you find convenient (pyscn, scn or psl). In the following example our target is to explore the mechnical behavior of a sofa force-field on a given range of parameters. 

Here is a very simple scene that we will use as an example: 
```xml
<Node name="Root" >
<OglModel filename="mesh/sphere.obj">
<GridTopology/>
<TetrahedronFEMForceField youngModulus="10000" 
  poissonRatio="0.4"/> 
</Node>
```

You can try the scene be starting it with runSofa. 


# Transform the scene into a scene template
Sofa-launcher is using the Cheetah templating engine. Its a very easy and powerful template engine.
To templatize the previously presented scene on the youngModulus & poissonRatio you simply have to do:
```xml
<Node name="Root" >
<OglModel filename="mesh/sphere.obj">
<GridTopology/>
<TetrahedronFEMForceField youngModulus="$YOUNGMODULUS" 
  poissonRatio="$POISSONRATIO"/> 
</Node>
```

This simply means that sofa-launcher will replace '$YOUNGMODULUS' and '$POISSONRATIO' before to start the simulations. 

# Write a python script to start the launcher and process the results. 
```python
import launcher
   
## This are the different files composing our scene
filenames = ["example.scn","controller.py"]
filesandtemplates = []

## Sofa-launcher expects the data to be given as a list of
## (filecontent, filename) so we build that
for filename in filenames:
	filesandtemplates.append( (open(filename).read(), filename) )

print("==================== NOW USING SEQUENTIAL LAUNCHER ===================")
results = startSofa([ 
	{"YOUNGMODULUS": "1", "POISSONRATIO": "0.33", "nbIterations":1000 },
	{"YOUNGMODULUS": "10", "POISSONRATIO": "0.43", "nbIterations":1000 },
	{"YOUNGMODULUS": "100", "POISSONRATIO": "0.53", "nbIterations":1000 },
	{"YOUNGMODULUS": "1000", "POISSONRATIO": "0.63", "nbIterations":1000 }], 
	filesandtemplates, launcher=SerialLauncher())

# All the run are now finished ! We can retrieve the run details & results 
# There is one entry per run
for res in results:
       print("Results: ")
       print("    directory: "+res["directory"])   #The place where the file for this run are stored
       print("scene: "+res["scene"])		   #Name of the scene 
       print("      logfile: "+res["logfile"])     #File that stores the run outputs to get value from the scene. 
       print("     duration: "+str(res["duration"])+" sec") 

```

# Get more complex data from the simulation.
It is very common that we want the script to process some information from the simulation. This easily be done
by printing in the console specific message using python script controller. These message are in the res.results field.
 
