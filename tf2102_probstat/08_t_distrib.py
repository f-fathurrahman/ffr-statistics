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

# Gaussian
populationY = stats.norm(loc=0.0, scale=1.0)

ν = 5
populationZ = stats.chi2(ν)

Nsamples = 100_000

samplesY = populationY.rvs(Nsamples)
samplesZ = populationZ.rvs(Nsamples)
tStats = samplesY/np.sqrt(samplesZ/ν)

num_bins = 100
idx_small = tStats < -4
idx_large = tStats > 4
idx_used = ~idx_small & ~idx_large
fig, ax = plt.subplots()
ax.hist(tStats[idx_used], num_bins, density=True, label="tStats")
ax.set_xlim(-4,4)
# The histogram is long tailed, we ignore some values beyond certain interval

t_rv = stats.t(ν)
xmin, xmax = ax.get_xlim()
NptsPlot = 200
xgrid = np.linspace(xmin, xmax, NptsPlot)
ax.plot(xgrid, t_rv.pdf(xgrid), label="theoretical")

ax.set_title("T distribution")
plt.savefig("IMG_07_t.png")
plt.show()
