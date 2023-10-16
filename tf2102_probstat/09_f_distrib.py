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

v1 = 5
populationV1 = stats.chi2(v1)

v2 = 3
populationV2 = stats.chi2(v2)

Nsamples = 100_000

samplesV1 = populationV1.rvs(Nsamples)
samplesV2 = populationV2.rvs(Nsamples)
fStats = (samplesV1/v1) / (samplesV2/v2)

plt.clf()
idx_used = fStats <= 10.0
num_bins = 80
plt.hist(fStats[idx_used], num_bins, density=True, label="fStats")

f_rv = stats.f(v1, v2)
xmin, xmax = plt.gca().get_xlim()
NptsPlot = 200
xgrid = np.linspace(xmin, xmax, NptsPlot)
plt.plot(xgrid, f_rv.pdf(xgrid), label="theoretical")

plt.title("F distribution")
plt.savefig("IMG_09_f.png")
plt.show()
