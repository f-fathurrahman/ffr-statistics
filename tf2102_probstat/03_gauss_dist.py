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

μ = -2.5
σ = 1.2
rv = stats.norm(loc=μ, scale=σ)

samples = rv.rvs(10000)

plt.clf()

# Using plt.stairs
# Calculate histogram
num_bins = 40

#counts, bins = np.histogram(samples, num_bins, density=True)
#plt.stairs(counts, bins, label="Histogram")
#
# Using plt.hist
#plt.hist(bins[:-1], num_bins, weights=counts, label="Histogram")
# FIXME: this seems to be a bit off

plt.hist(samples, num_bins, density=True)

xmin, xmax = plt.gca().get_xlim()
NptsPlot = 200
xgrid = np.linspace(xmin, xmax, NptsPlot)
plt.plot(xgrid, rv.pdf(xgrid), label="pdf")

plt.legend()
plt.savefig("IMG_03_gauss_hist.png")
plt.show()
