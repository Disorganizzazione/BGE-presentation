import bge
import aud 

device = aud.device()
sound = aud.Factory.file(bge.logic.expandPath("//soundtrack.wav"))
sound_handle = device.play(sound)   # sound.reverse would play the song in reverse
sound_handle.loop_count = -1   # loops endlessly