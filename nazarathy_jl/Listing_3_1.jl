using StatsBase, Plots

using PlotThemes
theme(:dark)

names = ["Mary", "Mel", "David", "John", "Kayley", "Anderson", "ffr", "fff"]

randomName() = rand(names)

X = 3:8
N = 10^6
sampleLengths = [length(randomName()) for _ in 1:N]

bar(X, counts(sampleLengths)/N, ylims=(0,0.35),
    xlabel="Name length", ylabel="Estimated p(x)", legend=:none)
