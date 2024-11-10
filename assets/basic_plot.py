#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# basic_plot.py

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

AVG2 = 10  # distance from average


def get_y(len_x, i):
    """ Getting y values for x """

    l0 = i*AVG2
    l1 = l0 + AVG2
    data = np.random.randint(l0, l1, len_x)
    return data


colors = ["darkorange", "olivedrab", "slateblue", "blueviolet"]
plot_nr = len(colors)
len_data = 30

fig, ax = plt.subplots()
fig.suptitle("Random data series", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

# for i in [2]:
for i in range(plot_nr):
    data = get_y(len_data, i)
    ax.plot(range(len_data), data, lw=2,
            color=colors[i], linestyle="-", label=f"data_{i}")
# plt.savefig("cos_x.png", dpi=120)
ax.set_ylim(-1, plot_nr*AVG2 + 1)
plt.legend()
plt.tight_layout()
plt.show()
