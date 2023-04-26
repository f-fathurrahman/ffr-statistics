import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np

np.random.seed(seed=1)

x = np.concatenate([
    5 + norm.rvs(loc=0, scale=0.5, size=10),
    2 + norm.rvs(loc=0, scale=0.2, size=10),
    5 + norm.rvs(loc=0, scale=0.1, size=10)
])

ax = pd.Series(x).plot(style=".", color="black")
ax.set_ylabel("Values")
ax.set_xlabel("Index")
ax.set_ylabel("Weight")

ax.hlines(y=5, xmin=0, xmax=9, color="darkgray")
ax.hlines(y=2, xmin=10, xmax=19, color="darkgray")
ax.hlines(y=5, xmin=20, xmax=29, color="darkgray")

ax.text(4, 6.5, "A")
ax.text(14, 3.5, "B")
ax.text(24, 6.5, "C")
ax.set_ylim(0, 8)

plt.savefig("IMG_Fig_1_4.png", dpi=150)
plt.show()
