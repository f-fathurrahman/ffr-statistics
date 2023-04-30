using Distributions, Plots

μ = 10.0
σ = 4.0

n = 10
N = 10^6

sMeans = zeros(Float64, N)
sVars = zeros(Float64, N)
tStats = zeros(Float64, N)

for i in 1:N
    data = rand(Normal(μ, σ), n)
    sampleMean = mean(data)
    sampleVars = var(data)
    sMeans[i] = sampleMean
    sVars[i] = sampleVars
    tStats[i] = (sampleMean - μ)/sqrt(sampleVars/n)
end

xRangeMean = 5:0.1:15
xRangeVar = 0:0.1:60
xRangeTStat = -5:0.1:5

p1 = stephist(sMeans, bins=50, normed=true, legend=false)
p1 = plot!(xRangeMean, pdf.(Normal(μ, σ/sqrt(n)), xRangeMean),
    xlims=(5, 15), ylim=(0, 0.35),
    xlabel="Sample means", ylabel="Density")

p2 = stephist(sVars, bins=50, normed=true, label="Simulated")
p2 = plot!(xRangeVar, (n-1)/σ^2*pdf.(Chisq(n-1), xRangeVar*(n-1)/σ^2),
    label="Analytic", xlims=(0,60), ylims=(0,0.06),
    xlabel="Sample Variance",ylabel="Density")

p3 = stephist(tStats, bins=100, normed=true, legend=false)
p3 = plot!(xRangeTStat, pdf.(TDist(n-1), xRangeTStat),
    xlims=(-5,5), ylims=(0,0.4), xlabel="t-statistic", ylabel="Density")

plot(p1, p2, p3, layout = (1,3), size=(1200, 800))

