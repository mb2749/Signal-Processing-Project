import numpy as np
import matplotlib.pyplot as plt

# Time axis
sample_freq = 1000
duration = 1

t = np.linspace(0, duration, sample_freq, endpoint=False)

# Creating a signal
freq = 10
signal = (
    np.sin(2 * np.pi * 10 * t)
    + 0.5 * np.sin(2 * np.pi * 30 * t)
    + 0.25 * np.sin(2 * np.pi * 70 * t)
)

# Creating noise
noise = np.random.normal(0, 2, len(t))

# Adding noise to the signal
noisy_signal = signal + noise

# Plotting signals
plt.figure(figsize=(10,8))

#Plotting clean signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Clean Signal")

# Plotting noisy signal
plt.subplot(2, 1, 2)
plt.plot(t, noisy_signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Noisy Signal")

plt.tight_layout()
plt.show()
