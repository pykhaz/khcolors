#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# basic_plot.py

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')


def get_y(len_x, i):
    """ Gettiong y values for x """

    dl = 10
    l0 = i*dl
    l1 = l0 + dl
    print(f"DBG: {l0 = }, {l1 = }")
    window_size = 3
    # hf = 0.2  # "height" factor
    # hf = 0.5  # "height" factor
    hf = 1  # "height" factor
    data = np.random.randint(l0, l1, len_x)
    smoothed_data = np.convolve(
        data, np.ones(window_size)/(window_size*hf), mode='valid')
    return data, smoothed_data


plot_nr = 3
len_raw = 30

# colors = ["#55FF55", "#5555FF", "#FFFF55"]
colors = ["darkorange", "olivedrab", "slateblue"]

# for i in [2]:
for i in range(plot_nr):
    y_raw, y_smooth = get_y(len_raw, i)
    x_raw = range(len(y_raw))
    x_smooth = range(len(y_smooth))
    plt.plot(x_raw, y_raw, lw=2,
             color=colors[i], linestyle="-", label=f"raw {i}")
    # plt.plot(x_smooth, y_smooth, lw=2,
    #          color="blue", linestyle="-", label=f"smooth {i}")
# plt.savefig("cos_x.png", dpi=120)
plt.legend()
plt.show()
