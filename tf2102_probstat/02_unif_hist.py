import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use("dark_background")
matplotlib.rcParams.update({
    "axes.grid" : True,
    "grid.color": "gray",
    "grid.linestyle": "--",
    "font.size": 12,
    "savefig.dpi": 150
})

rv = stats.uniform()
# Samples
samples = rv.rvs(10000)
plt.hist(samples, bins=50, density=True)
xgrid = np.linspace(-5.0, 5.0, 200)
plt.plot(xgrid, rv.pdf(x), label="pdf")
plt.legend()
plt.savefig("IMG_02_unif_hist.png")
plt.show()
