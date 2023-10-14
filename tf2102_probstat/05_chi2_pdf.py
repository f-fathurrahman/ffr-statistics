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

df = 3
rv = stats.chi2(df)

plt.clf()
NptsPlot = 200
xgrid = np.linspace(0.0, 10.0, NptsPlot)

plt.plot(xgrid, rv.pdf(xgrid), label="pdf")
plt.plot(xgrid, rv.cdf(xgrid), label="cdf")

plt.legend()
plt.savefig("IMG_05_chi2.png")
plt.show()

# table: example
# \chi2_α = 1 - cdf(0.115)