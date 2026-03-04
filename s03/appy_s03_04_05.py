#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:02:47 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array
a = numpy.array ([ [1.0, 2.0, 3.0], [100.0, 200.0, 300.0] ])

# printing Numpy array "a"
print (f'a:')
print (f'{a}')

# making a transposed array
b = a.T

# printing Numpy array "b"
print (f'b:')
print (f'{b}')
