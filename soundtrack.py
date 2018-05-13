import aud
import time

device = aud.device()
sound = aud.Factory.file("/home/harisont/Documents/blender-presentations/soundtrack.wav")
sound_handle = device.play(sound)
sound_handle.pitch = 3
#sound_handle.loop(-1)   # loops endlessly
