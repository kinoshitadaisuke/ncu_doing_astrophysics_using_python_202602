#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:31:31 (UT+08:00) daisuke>
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
