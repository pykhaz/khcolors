# cos_sin_x.py

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

color_cos = "yellowgreen"
color_sin = "orange"

color_label_cos = "lawngreen"
color_label_sin = "orangered"

x = np.linspace(0, 2*np.pi, 360, endpoint=True)
cos_x, sin_x = np.cos(x), np.sin(x)

fig, ax_0 = plt.subplots(figsize=(8, 6))
ax_0.set_title("cos(x) and sin(x)", fontsize=16)

color_sincos = "mediumslateblue"
color_label_cos = "lawngreen"
color_label_sin = "orangered"
color_label_sincos = "slateblue"

nr_pts = 1000
x = np.linspace(0, 2*np.pi, nr_pts, endpoint=True)
cos_x, sin_x = np.cos(x), np.sin(x)
sin_x_cos_x = sin_x*cos_x

fig, ax_0 = plt.subplots(figsize=(8, 6))
ax_0.set_title("sin(x), cos(x) and sin(x)*cos(x)", fontsize=16)

ax_1 = ax_0.twinx()

ax_0.plot(x, cos_x, lw=3, color=color_label_cos, label='cos(x)')
ax_1.plot(x, sin_x, lw=3, color=color_sin, label='sin(x)')


ax_0.set_xlabel("x", fontsize=14)
ax_0.set_ylabel("cos(x)", color=color_cos, fontsize=14)
ax_1.set_ylabel("sin(x)", color=color_sin, fontsize=14)
ax_1.set_yticks([])

ax_1.plot(x, sin_x_cos_x, lw=3, color=color_sincos, label='sin(x)*cos(x)')

ax_0.set_xlabel("x", fontsize=14)
ax_0.set_ylabel("sin(x)", color=color_sin, fontsize=14)
ax_1.set_ylabel("cos(x)", color=color_cos, fontsize=14)
ax_1.set_yticks([])

max_value = np.max(sin_x_cos_x)
max_idx = np.argmax(max_value)
tolerance = 1e-6
max_idc = np.where(np.isclose(sin_x_cos_x, max_value, atol=tolerance))[0]
x_annot = x[max_idc[1]]
y_annot = sin_x_cos_x[max_idc[1]]
ax_1.annotate(
    'sin(x)*cos(x)',
    color=color_label_sincos,
    xy=(x_annot, y_annot),
    xytext=(4.5, 0.9),
    arrowprops=dict(facecolor='black',
                    shrink=0.05, width=1.5),
    fontsize=12
)

ax_0.legend(loc='lower right', fontsize=12)
ax_1.legend(loc='lower left', fontsize=12)

plt.tight_layout()
plt.savefig("cos_sin_x.png", dpi=120)
plt.show()
