import numpy as np
from scipy import stats

population = stats.norm(loc=2.0, scale=3.0)
μ = population.mean()
σ = population.std()


Nsamples = [3, 5, 10, 15, 20, 25, 30, 50]
Ndata = len(Nsamples)


def do_trials():
    list_s_biased = np.zeros(Ndata)
    list_s_unbiased = np.zeros(Ndata)
    for i in range(Ndata):
        n = Nsamples[i]
        sample = population.rvs(n)
        list_s_biased[i] = np.std(sample)
        list_s_unbiased[i] = np.std(sample, ddof=1)
    return list_s_biased, list_s_unbiased


# Average over Ntrials
Ntrials = 1000
list_s_biased, list_s_unbiased = do_trials()
for itrials in range(Ntrials):
    l1, l2 = do_trials()
    #
    list_s_biased += l1
    list_s_biased /= 2
    #
    list_s_unbiased += l2
    list_s_unbiased /= 2


import matplotlib.pyplot as plt
plt.clf()
plt.plot(Nsamples, abs(list_s_unbiased - σ), label="s2 unbiased", marker="o")
plt.plot(Nsamples, abs(list_s_biased - σ), label="s2 biased", marker="*")
plt.ylabel("error")
plt.xlabel("Nsamples")
plt.legend()
plt.grid(True)
plt.show()

