Controlling the W-Gripper
============================
In this part of the tutorial we are going to go through the differents step of the programmation and the control of the motors that actuate the grippers.

### Prerequisites
To follow this part of the tutorial, you will need a few things make sure you have the required material and install the required software before starting.

#### Material :
For the controlling part you will need :
 * One MakeBlock MegaPi microcontroller 
 * Two MakeBlock Stepper motor driver V1 model MRK2
 * The gripper prototype done following the fabrication part of this tutorial.
 * A multimeter
 * A 9V power supply with jack adapter
 * A small phillips screwdriver

#### Software:
Before begining the program you will need to install on your computer :
 *  Arduino software [(available here)](https://www.arduino.cc/en/Main/Software)
 *  MakeBlock-USB-Driver [(available here)](https://github.com/Makeblock-official/Makeblock-USB-Driver)
 *  MakeBlock-Libraries [(available here)](https://github.com/Makeblock-official/Makeblock-Libraries) _make sure to include the librairies in the arduino's librairies folder in order to use it._
 * TimerOne librairie [(available here)](https://playground.arduino.cc/Code/Timer1) _make sure to include the librairies in the arduino's librairies folder in order to use it._

### Preparation
First of all we are going to see how to connect the gripper, the driver and the board in order to program them and control the robot.

First take your MegaPi board and the two Stepper drivers. Plug the divers on the port 1 and 2 of the board.  

__TODO insert images__  

Then take the gripper and connect the motors cables to the plugs and plug them on the board. Make sure the cables are on the right order : if you are using the same motors as described in the fabrication, the order shall be _black (A+), green (A-), red (B-), blue (B+)_. You can check on the back of the board the pin name and assure your connections are correct.  

__TODO insert images__  

You shall make sure that if you're looking to the robot and the pulley are facing you, the motor on your right is plug to port 1 and the left one is plug to port 2. If they are plug not plug correctly they will be turning the wrong way.

The Makeblock board has an external alimentation for the motor. In order to power the motor you shall connect it with a 9V power supply. The switch just aside control the turning on. Make sure you don't turn it on unless you want to. 
With a multimeter, you can adjust the voltage send to the motor by adjusting the position of the potentiometer on the driver. We fixed the output voltage at 4V.

__TODO insert images__  

The gripper is ready, next step is the control. Let's now have a look on the programmation.

### Programmation
The programmation of the gripper's control is going to be done using arduino IDE and using the MakeBlock libraries. Those choices has been made beaucause of the ease of use of the materials and the libraries. _If you have never used arduino IDE before you can have a look here : [first step with arduino IDE ](http://www.arduino.org/learning/getting-started/first-steps-with-arduino-ide)._
In order to use the Makeblock and TimerOne libraires you have to make sure you've include it in your arduino librairies files, and include the file by writting this line in the top of your program :
```C++
#include "MeMegaPi.h"
#include "TimerOne.h"
```
If you want to have a first look on the control of stepper motors using the MekeBlock librairie, you can have a look on the example  _MegaPiOnBoardStepperTest_. Any way we will see each function we will be using from this librairie one by one.  
First of all you have to declare each motor we want to control. In this tutorial, we are going to use 2 steppers motors and we have put them on the port 1 and 2. We declare them in a table of MeStepperOnBoard (type imported from the MakeBlock library). This is the declaration:

```C++
MeStepperOnBoard stepper[2] {{SLOT_1},{SLOT_2}}; 
```
This declaration handle all the pin declaration that you may do if you were using a simple arduino board. It makes it more easy beacause we can abstract from all the materials conections of the pin.
  
The MakeBlock board work the same way as an arduino. This mean we have to define the two main functions of arudino _setup_ and _loop_. The setup function will handle all the code that will be done once when the programm starts. The loop will be called reapeatedly and executed has long as the board is connected.

In order to use the motors we must initialize them. For each motor, we can define its MaxSpeed, its acceleration, and its number of microstep. As we want the two motors to have the same behaviour, we shall fix the same parameters for both of them. We put this code in a function so we can call it in the arduino setup function.

```C++  
void StepperInit(){
    for(int i =0;i<2;i++){
      stepper[i].setMaxSpeed(100);
      stepper[i].setAcceleration(20000);
      stepper[i].setMicroStep(16);
      stepper[i].enableOutputs();// TODO tell what this function do or see if it's usefull
    }
}
```

To handle the motor's rotation the library provides us two function:
  * __stepper.move(_int_ number-of-micro-steps)__
  * __stepper.moveTo(_int_ position)__
Thoose function will store the desired position to make the rotation, you must call the function __stepper.run()__. Each time it is called, the motor will make one microstep toward the desired position.

As we are currently handling two motors and we want them to sychronize and rotate on opposite directions we can define several function that will handle it :

```C++
void StepperMoveTo(int value)
{
    stepper[0].moveTo(-value);
    stepper[1].moveTo(value);   
}
void StepperMove(int value)
{
    stepper[0].move(-value);
    stepper[1].move(value);   
}

void StepperRun()
{
    stepper[0].run();
    stepper[1].run();   
}
```
As we want the motor to run repeatedly we can for now put it in the loop function. Our mains arudino's function actually look like this:
```C++
void setup()
{
	 StepperInit();
}

void loop()
{
   StepperRun();
}
```
The problem is we actually want to be able to control the rotation of the motors and send the wanted position to the arduino so he command the motors to move so. In order to communicate with the arduino, we will use Serial communication ([for more information see Serial] (https://www.arduino.cc/en/Reference/Serial). Serial communication must be initialized by setting the frequency of the communication by using __Serial.begin(_int_ frequency)__. So we will but that line of code in the setup function.

```C++
	 Serial.begin(9600);
```
In the arduino IDE you can open a serial communication by clicking on the magnifying glass icone. You must be connected to the board before doing this.

__TODO tell what is the board's name with a computer that have the USB driver installed and how to connect to it__

To catch the sended values, you may use sevral Serial functions:
 * __Serial.available()__ return a boolean that told us wether data have been received (true) or not (false).
 * __Serial.parseInt()__ read the availables data, parse it as an integer if possible and return it or return 0 if the data isn't an integer. With this code we can catch the value and pass it to the function __StepperMove()__ or __StepperMoveTo()__.

```C++
 long value;
  if(Serial.available()>1)
  {
    value = Serial.parseInt();
    Serial.print("value : ");
    Serial.println(value);
  }
  StepperMoveTo(value);
```
Now our first code version look like this and we can handle a first control of the position:

```C++
#include "TimerOne.h"
#include "MeMegaPi.h"

MeStepperOnBoard stepper[2] {{SLOT_1},{SLOT_2}}; 

void StepperMoveTo(int value)
{
    stepper[0].moveTo(-value);
    stepper[1].moveTo(value);   
}
void StepperMove(int value)
{
    stepper[0].move(-value);
    stepper[1].move(value);   
}

void StepperRun()
{
    stepper[0].run();
    stepper[1].run();   
}

void StepperInit()
{
   for(int i =0;i<2;i++)
    {
      // Change these to suit your stepper if you want
      stepper[i].setMaxSpeed(100);
      stepper[i].setAcceleration(20000);
      stepper[i].setMicroStep(16);
      stepper[i].enableOutputs();
  
    }
}

void setup()
{ 
	 Serial.begin(9600); 
	 StepperInit();
}

void loop()
{
  long value;
  if(Serial.available()>1)
  {
    value = Serial.parseInt();
    StepperMoveTo(value);
  }
}
```

__TODO explain the timerOne use and how it works__

final version:
```C++
#include "TimerOne.h"
#include "MeMegaPi.h"

MeStepperOnBoard stepper[2] {{SLOT_1},{SLOT_2}}; 

void StepperMoveTo(int value)
{
    stepper[0].moveTo(-value);
    stepper[1].moveTo(value);   
}
void StepperMove(int value)
{
    stepper[0].move(-value);
    stepper[1].move(value);   
}

void StepperRun()
{
    stepper[0].run();
    stepper[1].run();   
}

void StepperInit()
{
   for(int i =0;i<2;i++)
    {
      // Change these to suit your stepper if you want
      stepper[i].setMaxSpeed(100);
      stepper[i].setAcceleration(20000);
      stepper[i].setMicroStep(16);
      stepper[i].enableOutputs();
  
    }
  Timer1.initialize(100);
  Timer1.attachInterrupt(StepperRun);
}

void setup()
{ 
	 Serial.begin(9600); 
	 StepperInit();
}

void loop()
{
  long value;
  if(Serial.available()>1)
  {
    value = Serial.parseInt();
    StepperMoveTo(value);
  }
}
```
