#Merging Data Frames
import pandas as pd
import numpy as np

### binomial distribution
x =np.random.binomial(20, 0.5, 10000)  # 10000 simulation of flipping a fair coin 20 times
print((x>=15).mean())

# what a change of tornado
chance_of_tornado = 0.01/100
x = np.random.binomial(100000, chance_of_tornado)  # 100000 days, how many with tornado
print(x)

chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j] ==1 and tornado_events[j-1] == 1:
        two_days_in_a_row+=1
print(two_days_in_a_row)
### the above process is sampling process


# uniform distribution(continuous)
np.random.uniform(0,1)

# Normal/Gaussian distribution(continuous)
np.random.normal(0.75)  # mean = 0.75, variance= 1.0
x = np.random.normal(0.75,size=10000000)
np.sqrt(np.sum((np.mean(x)-x)**2/len(x)))
np.std(x)

import scipy.stats as stats
stats.kurtosis(x)
# the shape of tails of the distribution,
# negative value means the curve is slightly more flat than a normal distribution
# positive value means the curve is slightly more peaky than a normal distribution

stats.skew(x)
# We could also move out of the normal distributions and
# push the peak of the curve one way or the other. And this is called the skew.

# Chi Squared distribution, is left skewed, 1-parameter: degree of freedom
# left skewed means shift to left, positive; if negative, means shift to right
chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)

chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df2)

import matplotlib
import matplotlib.pyplot as plt
output = plt.hist([chi_squared_df2, chi_squared_df5], bins=50, histype="line", label=["2 DOF", "5 DOF"])
plt.legend(loc="upper right")

### modality
# for example, Bimodal distributions( can be simulated with 2 Gaussian distributions)


###Hypothesis Testing

# Hypothesis: a statement we can test
# Alternative Hypothesis: our idea, e.g. there is a differece between groups
# Null Hypothesis: the alternative of our idea, e.g. there is no difference between groups

df = pd.read_csv("C:\_research\coursera_pythonds\grades.csv")
df.shape

early = df[df["assignment1_submission"]<="2015-12-31"]
late = df[df["assignment1_submission"]>="2015-12-31"]
early.mean()
late.mean()

# Critical Value aplha
# The threshold as to how much chance you are willing to accept
# Typical values in social scienes are 0.1, 0.05, 0.01

from scipy import stats
stats.ttest_ind?
# t-test is a way to compare the means of 2 different populations
stats.ttest_ind(early["assignment1_grade"],late["assignment1_grade"])
# here is p-value(0.16) is much larger than 0.05, so not reject null hypothesis, so no difference
# namely no sitatistically difference

# run more t-tests, more likely to find a positive result just because of # of tests
# this called p-hacking or dredging and a serious methodological issue

# at a CI of 0.05, we expect to find one positive result I time out of 20 tests
# remedies:
# Bonferroni correction; strict alpha values with more tests.(alpha /n)  usually conservative
# Hold-out sets;  for example split into 2 datasets,
# Investigation pre-registration:

