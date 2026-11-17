import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import sys
sd.default.samplerate = 44100
sd.default.channels = 2

x = np.arange(-10, 10, 0.1)
data = np.sin(44100 * x)
print(data)

fig, ax = plt.subplots()
ax.plot(x, data)
fig.savefig("test.png")

sd.play(data)
sd.wait()