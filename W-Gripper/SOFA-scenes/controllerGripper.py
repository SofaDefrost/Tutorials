#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import Sofa
import time

count = 0



#def moveRestPos(rest_pos, dx, dy, dz):
    #str_out = ' '
    #for i in xrange(0,len(rest_pos)) :
        #str_out= str_out + ' ' + str(rest_pos[i][0]+dx)
        #str_out= str_out + ' ' + str(rest_pos[i][1]+dy)
        #str_out= str_out + ' ' + str(rest_pos[i][2]+dz)
    #return str_out


class controller(Sofa.PythonScriptController):


    def initGraph(self, node):

            self.node = node
            self.fingerNode=self.node.getChild('finger')
            self.cylinderNode=self.node.getChild('cylinder')
            self.cylinder2Node=self.node.getChild('cylinder2')



    #def onKeyPressed(self,c):

    def onBeginAnimationStep(self, dt):
            global count
            count = count + 1;
            print 'count = ' + str(count)
            self.dt = self.node.findData('dt').value
            print 'time1 = ' + str(self.dt)
            incr = 1;
	    incrV = 1.0;
            #disprotation1=0;
            #disprotation2=0;
            disp1=0;
            disp2=0;
            incr = 0.25;
	    incrV = 2.0;
	    #step=1;
            #global count;
            print disp1


            #if (c=="/"):

            #if (disp1 >= 64 & disprotation1 != 10):
		    #while(disp1 != 64):
            if (count <= 35):
                    self.cylinderNode.getObject('cylinderMO').findData('velocity').value = "0 0 0 0 0 0"
                    self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value = "0 0 0 0 0 0"
                    if (count <= 35):
                        print self.cylinderNode.getObject('cylinderMO').findData('velocity').value[0][5]
                        disp1 = self.cylinderNode.getObject('cylinderMO').findData('position').value[0][0] - incr
                        self.cylinderNode.getObject('cylinderMO').findData('position').value = disp1
                        disp2 = self.cylinder2Node.getObject('cylinder2MO').findData('position').value[0][0] - incr
                        self.cylinder2Node.getObject('cylinder2MO').findData('position').value = disp2
                        print 'first step, count is : ' + str(count)



            if (count > 35):
                if (count <= 43):
                    vel1 = self.cylinderNode.getObject('cylinderMO').findData('velocity').value[0][5] + incrV
                    self.cylinderNode.getObject('cylinderMO').findData('velocity').value = "0 0 0 0 0 "+str(vel1)
                    vel2 = self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value[0][5] - incrV
                    self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value = "0 0 0 0 0 "+str(vel2)
                    print 'second step, count is : ' + str(count)



                if (count > 43):

                    self.cylinderNode.getObject('cylinderMO').findData('velocity').value = "0 0 0 0 0 0"
                    self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value = "0 0 0 0 0 0"
                    if (count <= 78):
                        print self.cylinderNode.getObject('cylinderMO').findData('velocity').value[0][5]
                        disp1 = self.cylinderNode.getObject('cylinderMO').findData('position').value[0][0] + incr
                        self.cylinderNode.getObject('cylinderMO').findData('position').value = disp1
                        disp2 = self.cylinder2Node.getObject('cylinder2MO').findData('position').value[0][0] + incr
                        self.cylinder2Node.getObject('cylinder2MO').findData('position').value = disp2




#third step up






#second step turn



    def onKeyPressed(self,c):

            if (c == "+"):
		print self.cylinderNode.getObject('cylinderMO').findData('velocity').value[0]
                vel1 = self.cylinderNode.getObject('cylinderMO').findData('velocity').value[0][5] + incrV
                self.cylinderNode.getObject('cylinderMO').findData('velocity').value = "0 0 0 0 0 "+str(vel1)
                vel2 = self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value[0][5] - incrV
                self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value = "0 0 0 0 0 "+str(vel2)

            if (c == "-"):
                vel1 = self.cylinderNode.getObject('cylinderMO').findData('velocity').value[0][5] - incrV
                self.cylinderNode.getObject('cylinderMO').findData('velocity').value = "0 0 0 0 0 "+str(vel1)
                vel2 = self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value[0][5] + incrV
                self.cylinder2Node.getObject('cylinder2MO').findData('velocity').value = "0 0 0 0 0 "+str(vel2)


            if (ord(c) == 19):
                disp1 = self.cylinderNode.getObject('cylinderMO').findData('position').value[0][0] + incr
                self.cylinderNode.getObject('cylinderMO').findData('position').value = disp1
                disp2 = self.cylinder2Node.getObject('cylinder2MO').findData('position').value[0][0] + incr
                self.cylinder2Node.getObject('cylinder2MO').findData('position').value = disp2



            if (ord(c) == 21):
                disp1 = self.cylinderNode.getObject('cylinderMO').findData('position').value[0][0] - incr
                self.cylinderNode.getObject('cylinderMO').findData('position').value = disp1
                disp2 = self.cylinder2Node.getObject('cylinder2MO').findData('position').value[0][0] - incr
                self.cylinder2Node.getObject('cylinder2MO').findData('position').value = disp2
