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
ydata = []


for i, bi in enumerate(bands):
    ax[0, i].set_xticks([])
    ax[1, i].set_xticks([])
    # ax[0, i].set_rticks([])
    # ax[1, i].set_rticks([])
    ax[0, i].set_yticks([])
    ax[1, i].set_yticks([])


def update(frame):

    for i, bi in enumerate(bands):
        ax[0, i].clear()
        ax[1, i].clear()
        ax[0, i].set_xticks([])
        ax[1, i].set_xticks([])
        ax[0, i].set_yticks([])
        ax[1, i].set_yticks([])

        bb = b[bi, frame]
        if b.real.nonzero()[0].any():
            pm_polar(ax[0, i], t, bb.real, colors)
        if b.imag.nonzero()[0].any():
            pm_polar(ax[1, i], t, bb.imag, colors)


# frames = np.stack([
    # np.concatenate([np.linspace(bi, 1.0, 100), np.linspace(1.0, bi, 100)])
    # for bi in bands], 0)
frames = np.stack([
    np.concatenate([np.full(20, bi), np.linspace(bi, 1.0, 100),
                    np.ones(20), np.linspace(1.0, bi, 100),
                    np.full(20, bi)])
    for bi in bands], 0)
b = np.exp(1j * frames[..., None] * t[None, None, :])
ani = FuncAnimation(
    fig, update, frames=np.arange(frames.shape[1]), interval=10, repeat=True)
plt.show()

