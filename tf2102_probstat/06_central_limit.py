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
#μ = -2.5
#σ = 1.2
#population = stats.norm(loc=μ, scale=σ)

#population = stats.uniform(loc=-5.0, scale=10) # random [-5,5]
#μ = population.mean()
#σ = population.std()

population = stats.binom(10, 0.2)
μ = population.mean()
σ = population.std()

print("Mean of population = %.6f" % μ)
print("std of population  = %.6f" % σ)

Ntrials = 20000
Nsamples = 100

sample_means = np.zeros(Ntrials)
sample_stdevs = np.zeros(Ntrials)
tStats = np.zeros(Ntrials)

for i in range(Ntrials):
    sample = population.rvs(Nsamples)
    sample_means[i] = np.mean(sample)
    sample_stdevs[i] = np.std(sample, ddof=1)
    tStats[i] = (np.sum(sample) - Nsamples*μ)/(σ*np.sqrt(Nsamples))

print()
print("Mean of sample_means = %.6f" % np.mean(sample_means))
print("std of sample_means  = %.6f" % np.std(sample_means))

print()
print("Mean of sample_stdevs = %.6f" % np.mean(sample_stdevs))
print("std of sample_stdevs  = %.6f" % np.std(sample_stdevs))

num_bins = 40

fig, ax = plt.subplots(1, 2)

ax[0].hist(sample_means, num_bins, density=True, label="sample means")
ax[0].set_title("Sample means distribution")

ax[1].hist(tStats, num_bins, density=True)
ax[1].set_title("t-statistic distribution")

plt.savefig("IMG_06_central_limit.png")
plt.show()
