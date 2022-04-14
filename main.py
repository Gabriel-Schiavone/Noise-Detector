import sounddevice as sd
import numpy as np
import simpleaudio as sa

sensitivity = int(input("Please enter a trigger level: "))
sound = sa.WaveObject.from_wave_file("sound.wav")


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print(int(volume_norm))
    if volume_norm >= sensitivity:
        play_obj = sound.play()
        play_obj.wait_done()


with sd.Stream(callback=print_sound):
    sd.sleep(-1)
