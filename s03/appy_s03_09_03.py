#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:13:39 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10 random numbers of uniform distribution between 0 and 1
array_x = rng.random (10)

# printing generated random numbers
print (f'{array_x}')
