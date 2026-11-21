import math
from scipy.stats import binom

# Parameters
n = 30                 # number of days
p = 10 / 30            # daily rain probability (expected 10 days)

# Cumulative distribution function (CDF) from scipy
# CDF(k) = P(X <= k)

# Probability of 12 or more rainy days
p_ge_12 = 1 - binom.cdf(11, n, p)

# Probability of between 12 and 18 rainy days (inclusive)
p_between = binom.cdf(18, n, p) - binom.cdf(11, n, p)

print(f"Probability of >= 12 rainy days: {p_ge_12:.6f}")
print(f"Probability of 12 <= X <= 18 rainy days: {p_between:.6f}")