import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

frequency = 5

signal = np.sin(2 * np.pi * frequency * t)

plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("First Signal")
plt.show()
