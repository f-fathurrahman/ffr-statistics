import numpy as np
from scipy import stats

population = stats.norm(loc=2.0, scale=1.0)
μ = population.mean()
σ = population.std()


Nsamples = 5

Ntrials = 1000
s_biased = np.zeros(Ntrials)
s_unbiased = np.zeros(Ntrials)

for i in range(Ntrials):
    sample = population.rvs(Nsamples)
    s_biased[i] = np.std(sample)
    s_unbiased[i] = np.std(sample, ddof=1)

print("s true = ", σ)

print("mean s_biased = ", np.mean(s_biased))
print("mean s_unbiased = ", np.mean(s_unbiased))

import matplotlib.pyplot as plt
plt.clf()
plt.plot(np.abs(s_unbiased - σ), label="s2 unbiased")
plt.plot(np.abs(s_biased - σ), label="s2 biased")
plt.ylabel("error")
plt.xlabel(f"Nsamples = {Nsamples}")
plt.legend()
plt.grid(True)
plt.show()

