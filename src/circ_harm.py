import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
from circular_bands import pm_polar


colors = ['#ef8a62', '#67a9cf']
N = 1024
B = 7
t = np.linspace(0, 2*np.pi, N)
bands = np.arange(B)
b = np.exp(1j * bands[:, None] * t[None, :])

x = np.zeros_like(t)
x[0:N//2+0] = 1/(N//2)
# x[512:513] = 1.

xf = fftfreq(1024, 1. / 1024)[:1024//2]
X = fft(x)

fig, ax = plt.subplots(2, len(bands), subplot_kw={'projection': 'polar'})
for i, bi in enumerate(bands):
    # w = b[:bi+1, 100:N//2+100].conj().sum(1, keepdims=True)

    # Solution to the integral
    k = np.arange(bi+1)[:, None]
    w = N / (2 * np.pi * k) * (
        np.exp(-1j * 2 * np.pi * (N//2) * k / N + 1j * np.pi/2)
        - np.exp(1j * np.pi/2))
    w[0] = N//2

    # w = b[:bi+1, [512]]
    ix = np.sum(b[:bi+1] * w, axis=0)
    ax[0, i].set_rticks([])
    ax[1, i].set_rticks([])
    ax[0, i].set_xticks([])
    ax[1, i].set_xticks([])
    pm_polar(ax[0, i], t, ix.real, colors)
    pm_polar(ax[1, i], t, ix.imag, colors)
# plt.show()

fig, ax = plt.subplots(2, len(bands), subplot_kw={'projection': 'polar'})
for i, bi in enumerate(bands):
    ix = ifft(X[:bi+1], n=1024)

    ax[0, i].set_rticks([])
    ax[1, i].set_rticks([])
    ax[0, i].set_xticks([])
    ax[1, i].set_xticks([])
    pm_polar(ax[0, i], t, ix.real, colors)
    pm_polar(ax[1, i], t, ix.imag, colors)
plt.show()
