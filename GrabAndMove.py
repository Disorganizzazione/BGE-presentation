import bge
from mathutils import Vector

def main():

	cont = bge.logic.getCurrentController() #The Python controller of this Python script.
	own = cont.owner #The object the controller is attached to.
	Click = cont.sensors['lclick'] 
	
	if Click.positive:
		 cam = bge.logic.getCurrentScene().active_camera
		 offset = cam.worldPosition + (cam.worldOrientation*Vector([0,0,-20])) #camera offset
		 #Pick a object
		 if type(own['Grabbed']) is str: #Hit the object
			 Ray = cam.rayCast(offset) #Find first object hit within offset and (self) object center
			 if Ray[0]: #if collided
				 own['Grabbed']=Ray[0] #print('Hit', Ray[0])
		 else: #Move The Object
			 V= offset - own['Grabbed'].worldPosition #camera-grabbed object offset
			 own['Grabbed'].applyForce((V)*9.8*V.magnitude)
			 own['Grabbed'].worldLinearVelocity*=0.9
	else:
		own['Grabbed']='Empty'

main()