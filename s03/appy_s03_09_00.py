#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:13:11 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.default_rng ()

# generating a random number of uniform distribution between 0 and 1
array_x = rng.random ()

# printing generated random numbers
print (f'{array_x}')
