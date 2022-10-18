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
# fig, ax = plt.subplots(2, len(bands))
ydata = []
lns = [ax[c, i].plot([], [])[0] for c in range(2) for i in range(len(bands))]


def init():
    for i, bi in enumerate(bands):
        ax[0, i].set_xticks([])
        ax[1, i].set_xticks([])
        # ax[0, i].set_rticks([])
        # ax[1, i].set_rticks([])
        ax[0, i].set_yticks([])
        ax[1, i].set_yticks([])

        lns[i].set_data([], [])
        lns[len(bands) + i].set_data([], [])
    return lns


def update(frame):
    for i, bi in enumerate(bands):
        b = np.exp(1j * bi * frame * t)
        # if b.real.nonzero()[0].any():
            # pm_polar(ax[0, i], t, b.real, colors)
        # if b.imag.nonzero()[0].any():
            # pm_polar(ax[1, i], t, b.imag, colors)

        # c = np.chararray(b.shape[0], itemsize=7)
        # c[b.real > 0] = colors[0]
        # c[b.real <= 0] = colors[1]

        # lns[i].set_data(t[b.real > 0], b.real[b.real > 0])
        lns[i].set_data(t, b.real)
        lns[i].set_color(colors[0])
        lns[i].set_data(t, b.imag)
        lns[i].set_color(colors[1])
        # lns[i].set_data(t, b.real)

        # lns[i].set_data(t[b.real <= 0], b.real[b.real <= 0], colors[1])
        lns[len(bands) + i].set_data(t[b.imag > 0], b.imag[b.imag > 0])
    return lns


ani = FuncAnimation(fig, update, frames=np.linspace(1, 0, 128),
                    interval=25, init_func=init, blit=True, repeat=True)
plt.show()


