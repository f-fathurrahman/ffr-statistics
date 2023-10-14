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
# Plot pdf
x = np.linspace(-0.5, 1.5, 100)
plt.plot(x, rv.pdf(x), label="pdf")
plt.savefig("IMG_unif_pdf.png")
plt.show()
