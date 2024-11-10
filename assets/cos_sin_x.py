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
ax_1 = ax_0.twinx()

ax_0.plot(x, cos_x, lw=3, color=color_label_cos, label='cos(x)')
ax_1.plot(x, sin_x, lw=3, color=color_sin, label='sin(x)')

ax_0.set_xlabel("x", fontsize=14)
ax_0.set_ylabel("cos(x)", color=color_cos, fontsize=14)
ax_1.set_ylabel("sin(x)", color=color_sin, fontsize=14)
ax_1.set_yticks([])

ax_0.legend(loc='lower right', fontsize=12)
ax_1.legend(loc='lower left', fontsize=12)

plt.tight_layout()
plt.savefig("cos_sin_x.png", dpi=120)
plt.show()
