import bge
from mathutils import Vector

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner
	Click = cont.sensors['lclick']
	
	if Click.positive:
		 cam = bge.logic.getCurrentScene().active_camera
		 #Pick a object
		 if type(own['Grabbed']) is str:
			 offset = cam.worldPosition+(cam.worldOrientation*Vector([0,0,-own['Range']]))
             #collisiom
			 if cam.parent:
				 Ray = cam.parent.rayCast(offset, cam.worldPosition,0)
			 else:
				 Ray = cam.rayCast(offset, cam.worldPosition,0)
				 
			 if Ray[0]:
				 print('Hit')
				 own['Grabbed']=Ray[0]
		 else:
			 #Move The Object
			 offset = cam.worldPosition+(cam.worldOrientation*Vector([0,0,-20]))
			 V=offset-own['Grabbed'].worldPosition
			 own['Grabbed'].applyForce((V)*9.8*V.magnitude)
			 own['Grabbed'].worldLinearVelocity*=0.9	 
	else:
		own['Grabbed']='Empty'
		
main()
