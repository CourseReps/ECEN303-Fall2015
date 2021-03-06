__author__ = "Ben Johnston"
__NetID__ = "benj626"
__GitHubID__ = "benj626"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = "5"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt

ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    if random.random() < p:
        return 1
    else:
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []
for TrialIndex2 in range(0, NumberTrials):
    sum_inter = 0
    for InterIndex in range(0, NumberFlips):
        sum_inter += biasedcoinflip(ParameterP)
    SumTrials.append(sum_inter)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))
Sum_Distribion = 0
for slot in Distribution:
    Sum_Distribion += slot
print(repr(Sum_Distribution))

OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.

The graph shifts from the left to the right as ParameterP increases. Thus the more likely it is to achieve a one,
the more ones will show up, and vice versa. When ParameterP is set to either extreme, 0 or 1, the figure is entirely over 0 or 1
respectively as no other outcome is possible.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?

6 is the most likely outcome with a probability of 29.6%

"""
