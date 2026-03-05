#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:31:07 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# output file name
file_output = 'numpy_03.npy'

# a list
list_a = [ 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, -1.0, -2.0, -3.0, -4.0 ]

# making a Numpy array from a list
array_a = numpy.array (list_a)

# printing Numpy array
print (f'{array_a}')

# saving Numpy array into "npy" file
numpy.save (file_output, array_a)
