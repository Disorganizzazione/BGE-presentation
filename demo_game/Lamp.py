import bge
from mathutils import Vector

cont = bge.logic.getCurrentController() #The Python controller of this Python script.
for o in cont.sensors:
    own = o.owner #The object the controller is attached to.
    Click = o
    if Click.positive:
        print(own.color)
        own.color=(1,0,0)
    else:
        own.color=(0.004142059478908777, 0.39255815744400024, 1.0)