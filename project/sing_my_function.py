import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import sys
sd.default.samplerate = 44100
sd.default.channels = 2

t = 2
duration = t
f = 500
volume = 0.2
x = np.arange(0, duration, 1 / 44100)
data = volume * np.sin((2*np.pi) * f * x)


fig, ax = plt.subplots()
ax.plot(x, data)
# ax.set_xlim(0, 0.01)
fig.savefig("test.png")
print(len(data))
print(len(data) / 44100)

sd.play(data)
sd.wait()