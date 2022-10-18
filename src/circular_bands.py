import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


N = 1024
t = np.linspace(0, 2*np.pi, N)


def pm_polar(ax, t, x, colors):
    """Polar plot with different colors for positive and negative values"""
    ax.plot(t[x > 0], x[x > 0], colors[0])
    ax.plot(t[x <= 0], -x[x <= 0], colors[1])


colors = ['#ef8a62', '#67a9cf']
bands = np.arange(0, 6)
fig, ax = plt.subplots(2, len(bands), subplot_kw={'projection': 'polar'})
for i, bi in enumerate(bands):
    b = np.exp(1j * bi * t)
    if b.real.nonzero()[0].any():
        pm_polar(ax[0, i], t, b.real, colors)
    if b.imag.nonzero()[0].any():
        pm_polar(ax[1, i], t, b.imag, colors)
    ax[0, i].set_xticks([])
    ax[0, i].set_rticks([])
    ax[1, i].set_xticks([])
    ax[1, i].set_rticks([])
plt.show()

fig, ax = plt.subplots(2, len(bands), subplot_kw={'projection': 'polar'})
for i, bi in enumerate(bands):
    c = np.cos(bi * t)
    s = np.sin(bi * t)
    # if bi == 0:
        # c /= np.sqrt(2 * np.pi)
        # s /= np.sqrt(2 * np.pi)
    # else:
        # c /= np.sqrt(np.pi)
        # s /= np.sqrt(np.pi)

    if c.nonzero()[0].any():
        pm_polar(ax[0, i], t, c, colors)
    if s.nonzero()[0].any():
        pm_polar(ax[1, i], t, s, colors)

    ax[0, i].set_xticks([])
    ax[0, i].set_rticks([])
    ax[1, i].set_xticks([])
    ax[1, i].set_rticks([])
plt.show()
