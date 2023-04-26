import matplotlib.pyplot as plt
import math
from scipy.stats import norm

# Sinusoidal, deterministic part
x = [math.sin(x*2*math.pi/50) for x in range(1,51)]

# Add random, normal distributed, components
x = [xi + norm.rvs(loc=0, scales=0.05) for xi in x]

# Make a plot via Pandas
# Create a Series first, then plot
ax = pd.Series(x).plot(style=".", color="black")
ax.set_ylabel("Values")
ax.hline(y=0, linestyle="--", color="darkgray")
plt.savefig("IMG_Fig_1_3.png", dpi=150)
plt.show()
