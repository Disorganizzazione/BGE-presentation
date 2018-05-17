import bge
import time

cont = bge.logic.getCurrentController()
own = cont.owner    # reference to owner object

# sensors
up = cont.sensors["Up"]
shift = cont.sensors["Shift"]

# actuators & attributes
sound = cont.actuators["Soundtrack"]
pitch = sound.pitch

if shift.positive and up.positive:
    pitch += 0.1
else:
    pitch = 1
    
sound.pitch = pitch
cont.activate(sound)