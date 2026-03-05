#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:27:11 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# explicitly specify PCG64 for random number generator
rng = numpy.random.Generator (numpy.random.PCG64 ())

# generating a random number of uniform distribution between 0 and 1
array_x = rng.random ()

# printing generated random numbers
print (f'{array_x}')
