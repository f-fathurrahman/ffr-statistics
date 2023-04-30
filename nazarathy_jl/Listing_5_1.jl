using Random, Distributions, Plots

using PlotThemes
theme(:dark)

λ = 1/4.5
expDist = Exponential(1/λ)
n = 10
N = 10^6

means = Vector{Float64}(undef, N)
variances = Vector{Float64}(undef, N)

for i in 1:N
    data = rand(expDist, n)
    means[i] = mean(data)
    variances[i] = var(data)
end

println("Actual mean: ", mean(expDist))
println("Sample mean: ", mean(means))

println("Actual variance: ", var(expDist))
println("Sample variance: ", mean(variances))

stephist(means, bins=200, normed=true,
    label="Histogram of Sample Means")

stephist!(variances, bins=600, normed=true,
    label="Histogram of Sample Variances",
    xlims=(0,40), ylim=(0,0.4),
    xlabel="Statistic value", ylabel="Density")