import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100) # time sequence
y = np.sin(x)
fig, ax = plt.subplots() # makes figure with two variables define on one line
ax.plot(x, y)
ax.set_xlabel("time (s)")
ax.set_ylabel("amplitude")
ax.grid(alpha = 1) # grid and opacity

fig.savefig("/Users/hamilton/Desktop/Fall2026/astr119/tests/class_demos/wave.png")

