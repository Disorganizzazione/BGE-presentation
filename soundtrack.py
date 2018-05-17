import bge

cont = bge.logic.getCurrentController()
own = cont.owner    # reference to owner object
up = cont.sensors["Up"]
shift = cont.sensors["Shift"]
sound = cont.actuators["Soundtrack"]
pitch = sound.pitch

if shift.positive:
    pitch = 2

    
sound.pitch = pitch
cont.activate(sound)

