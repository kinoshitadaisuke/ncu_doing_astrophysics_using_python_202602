#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:30:19 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_00.data'

# opening and reading file and storing data in a Numpy array
data = numpy.loadtxt (file_input)

# printing data
print (f'{data}')
