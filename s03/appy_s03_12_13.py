#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:31:37 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_04.npz'

# loading Numpy arrays from npy file
arrays = numpy.load (file_input)

# printing "arrays"
print (f'{arrays}')

# printing object type of "arrays"
print (f'{type (arrays)}')

# first Numpy array in "arrays"
array_c = arrays['array_c']

# second Numpy array in "arrays"
array_d = arrays['array_d']

# printing array_c and array_d
print (f'array_c:')
print (array_c)
print (f'array_d:')
print (array_d)
