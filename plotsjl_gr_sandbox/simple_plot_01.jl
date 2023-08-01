Pkg.activate("statistics", shared=true)

using Plots
using PlotThemes

# Let's use dark theme
theme(:dark)

x = range(-1.0, 1.0, length=100) # similar to np.linspace
y1 = sinpi.(x)
y2 = cospi.(x)

# Initialize a figure
plot(title="This is plot title", dpi=200)
# Add a line
plot!(x, y1, label="sinpi", lw=2)
# Add another line
plot!(x, y2, label="cospi", lw=3)
# Set xlabel and ylabel
xlabel!("This is x label")
ylabel!("This is y label")


# This will save current figure
savefig("IMG_01.png")
savefig("IMG_01.pdf")

