import statistics as stats

# Data
data = [10, 20, 20, 30, 40, 50, 50, 50]

# Mean
mean = stats.mean(data)
print("Mean:", mean)

# Median
median = stats.median(data)
print("Median:", median)

# Mode
mode = stats.mode(data)
print("Mode:", mode)

# Standard Deviation
stdev = stats.stdev(data)
print("Standard Deviation:", stdev)

# Variance
variance = stats.variance(data)
print("Variance:", variance)