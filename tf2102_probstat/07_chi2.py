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
population = stats.norm(loc=0.0, scale=1.0)
μ = population.mean()
σ = population.std()

print("Mean of population = %.6f" % μ)
print("std of population  = %.6f" % σ)

Ntrials = 200_000
Nsamples = 10

χ2 = np.zeros(Ntrials)
samples = np.zeros(Nsamples)
for i in range(Ntrials):
    samples[:] = population.rvs(Nsamples)
    χ2[i] = np.sum(samples**2)

num_bins = 40
fig, ax = plt.subplots()
ax.hist(χ2, num_bins, density=True, label="sample means")

chi2_rv = stats.chi2(Nsamples)
# dof = Nsamples
xmin, xmax = ax.get_xlim()
NptsPlot = 200
xgrid = np.linspace(xmin, xmax, NptsPlot)
ax.plot(xgrid, chi2_rv.pdf(xgrid), label="theoretical")

ax.set_title("chi2 distribution")
plt.savefig("IMG_07_chi2.png")
plt.show()
