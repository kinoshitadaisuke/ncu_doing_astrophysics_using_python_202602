#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:22:13 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array
a = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

# printing Numpy array "a"
print (f'a:')
print (f'{a}')

# flattening of a Numpy array
b = numpy.matrix.flatten (a)

# printing Numpy array "b"
print (f'b:')
print (f'{b}')
