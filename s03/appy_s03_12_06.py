#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:24:37 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_01.data'

# opening and reading file and storing data in a Numpy array
data = numpy.loadtxt (file_input)

# printing data
print (f'{data}')

# object type of the object "data"
type_data = type (data)

# printing object type
print (f'object type = {type_data}')

# printing information of Numpy array
print (f'information:')
print (f'  ndim     = {data.ndim}')
print (f'  size     = {data.size}')
print (f'  shape    = {data.shape}')
print (f'  dtype    = {data.dtype}')
print (f'  itemsize = {data.itemsize} byte')
