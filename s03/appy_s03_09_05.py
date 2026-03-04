#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:14:28 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.Philox ())

# generating 100 random numbers of Gaussian distribution
# of mean of 100.0 and standard deviation of 10.0
array_x = rng.normal (100.0, 10.0, 100)

# printing generated random numbers
print (f'{array_x}')
