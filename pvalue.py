#!/usr/bin/env python

import sys
import numpy
from scipy import stats

samples = []

initial_sample_size = int(input("Initial sample size? "))

if initial_sample_size == 1:
    print("You'll need more samples than that. Let's try a sample size of 2.")
    initial_sample_size = 2

for i in range(initial_sample_size):
    samples.append(numpy.random.normal())

t, pvalue = stats.ttest_1samp(samples, 0.0)

while pvalue > 0.05:
    if len(samples) > 150:
        print("Your sample has gotten pretty big. Looks like there's no effect :(")
        sys.exit()
    print("Oops, your p-value is %1.5f; that's too big. Let's continue the experiment." % pvalue)
    next_sample_size = int(input("How many more samples? "))
    for i in range(next_sample_size):
        samples.append(numpy.random.normal())

    t, pvalue = stats.ttest_1samp(samples, 0.0)

print("You win! P-value is %1.5f!" % pvalue)
    
