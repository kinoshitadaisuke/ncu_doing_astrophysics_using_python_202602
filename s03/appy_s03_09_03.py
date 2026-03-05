#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:27:27 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10 random numbers of uniform distribution between 0 and 1
array_x = rng.random (10)

# printing generated random numbers
print (f'{array_x}')
