#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 19:59:14 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of 5x5 shape
# with all the elements initialised by one.
array_o = numpy.ones ( (5, 5) )

# printing Numpy array
print (f'array_o:\n{array_o}')

# printing information
print (f'information:')
print (f'  ndim     = {array_o.ndim}')
print (f'  size     = {array_o.size}')
print (f'  shape    = {array_o.shape}')
print (f'  dtype    = {array_o.dtype}')
print (f'  itemsize = {array_o.itemsize} byte')
