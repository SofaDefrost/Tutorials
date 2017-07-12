#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import Sofa


def moveRestPos(rest_pos, dx, dy, dz):
    str_out = ' '
    for i in xrange(0,len(rest_pos)) :
        str_out= str_out + ' ' + str(rest_pos[i][0]+dx)
        str_out= str_out + ' ' + str(rest_pos[i][1]+dy)
        str_out= str_out + ' ' + str(rest_pos[i][2]+dz)
    return str_out


class controller(Sofa.PythonScriptController):
    

            
    

    def initGraph(self, node):

            self.node = node
            self.finger1Node=self.node.getChild('finger1')
            self.finger2Node=self.node.getChild('finger2')
            self.finger3Node=self.node.getChild('finger3')    
            self.pressureConstraint1Node = self.finger1Node.getChild('cavity')
            self.pressureConstraint2Node = self.finger2Node.getChild('cavity')
            self.pressureConstraint3Node = self.finger3Node.getChild('cavity')

            
    def onKeyPressed(self,c):
        
            self.dt = self.node.findData('dt').value
            incr = self.dt*1000.0;
            
            print 'Key Pressed is: ', c
            self.MecaObject1=self.finger1Node.getObject('tetras');
            self.MecaObject2=self.finger2Node.getObject('tetras');
            self.MecaObject3=self.finger3Node.getObject('tetras');

            self.pressureConstraint1 = self.pressureConstraint1Node.getObject('SurfacePressureConstraint')
            self.pressureConstraint2 = self.pressureConstraint2Node.getObject('SurfacePressureConstraint')
            self.pressureConstraint3 = self.pressureConstraint3Node.getObject('SurfacePressureConstraint')

            if (c == "+"):
                print 'squeezing...'
                pressureValue = self.pressureConstraint1.findData('value').value[0][0] + 0.01
                self.pressureConstraint1.findData('value').value = str(pressureValue)
                pressureValue = self.pressureConstraint2.findData('value').value[0][0] + 0.01
                self.pressureConstraint2.findData('value').value = str(pressureValue)
                pressureValue = self.pressureConstraint3.findData('value').value[0][0] + 0.01
                self.pressureConstraint3.findData('value').value = str(pressureValue)

            if (c == "-"):
                print 'releasing...'
                pressureValue = self.pressureConstraint1.findData('value').value[0][0] - 0.01
                self.pressureConstraint1.findData('value').value = str(pressureValue)
                pressureValue = self.pressureConstraint2.findData('value').value[0][0] - 0.01
                self.pressureConstraint2.findData('value').value = str(pressureValue)
                pressureValue = self.pressureConstraint3.findData('value').value[0][0] - 0.01
                self.pressureConstraint3.findData('value').value = str(pressureValue)

            # UP key :
            if ord(c)==19:
                test1 = moveRestPos(self.MecaObject1.rest_position, 3.0, 0.0, 0.0)
                self.MecaObject1.findData('rest_position').value = test1
                test2 = moveRestPos(self.MecaObject2.rest_position, 3.0, 0.0, 0.0)
                self.MecaObject2.findData('rest_position').value = test2
                test3 = moveRestPos(self.MecaObject3.rest_position, 3.0, 0.0, 0.0)
                self.MecaObject3.findData('rest_position').value = test3
                
            

            # DOWN key : rear
            if ord(c)==21:
                test = moveRestPos(self.MecaObject1.rest_position, -3.0, 0.0, 0.0)
                self.MecaObject1.findData('rest_position').value = test
                test = moveRestPos(self.MecaObject2.rest_position, -3.0, 0.0, 0.0)
                self.MecaObject2.findData('rest_position').value = test
                test = moveRestPos(self.MecaObject3.rest_position, -3.0, 0.0, 0.0)
                self.MecaObject3.findData('rest_position').value = test


            # LEFT key : left
            if ord(c)==20:
                test = moveRestPos(self.MecaObject1.rest_position, 0.0, 3.0, 0.0)
                self.MecaObject1.findData('rest_position').value = test
                test = moveRestPos(self.MecaObject2.rest_position, 0.0, 3.0, 0.0)
                self.MecaObject2.findData('rest_position').value = test
                test = moveRestPos(self.MecaObject3.rest_position, 0.0, 3.0, 0.0)
                self.MecaObject3.findData('rest_position').value = test
                        
            
            # RIGHT key : right
            if ord(c)==18:
                test = moveRestPos(self.MecaObject1.rest_position, 0.0, -3.0, 0.0)
                self.MecaObject1.findData('rest_position').value = test
                test = moveRestPos(self.MecaObject2.rest_position, 0.0, -3.0, 0.0)
                self.MecaObject2.findData('rest_position').value = test
                test = moveRestPos(self.MecaObject3.rest_position, 0.0, -3.0, 0.0)
                self.MecaObject3.findData('rest_position').value = test


            

