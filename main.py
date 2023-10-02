import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np

import matplotlib           # see SO #73745245. seems to remember the backend to use is somewhat dependant on OS
matplotlib.use('TkAgg')

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
offset = 30
freq = 0.1
# Make data - instant coffee
X = np.arange(0, 40, 1)
Y = np.arange(0, 40, 1)
X, Y = np.meshgrid(X, Y)
R1 = np.sqrt(X ** 2 + Y ** 2)
R2 = np.sqrt((X-offset) ** 2 + (Y+offset) ** 2)
z_instant = np.sin(R1 / freq) * np.sin(R2 / freq)

# make date - americano
z_americano = np.full((40,40), 0.90)

# Plot the surface. Actually matplotlib is NOT very good to plot intersecting surfaces.... so just hacking it. basically merging my data and just plotting "one" dataset, whichever is greater
surf_americano = ax.plot_surface(X, Y, np.where(z_instant<z_americano, z_americano, z_instant), cmap=cm.coolwarm, linewidth=0, antialiased=False)
# surf_americano = ax.plot_surface(X, Y, z_instant, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# surf_instant = ax.plot_surface(X, Y, z_americano, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# surf_lesser = ax.plot_surface(X, Y, np.where(z_instant>=z_americano, z_americano, 0), cmap=cm.coolwarm, linewidth=0, antialiased=False)

# axis customiz.
# ax.set_zlim(0.8, 1.01)
ax.set_zlim(-1, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel("Time")
ax.set_ylabel("Africa vibes of the day")
ax.set_zlabel("Coffee desir intensity")

# colobar to look science-ish
fig.colorbar(surf_americano, shrink=0.5, aspect=5)
plt.title("Intensité du désir d'américano vs café instant de Francis")

plt.show()
