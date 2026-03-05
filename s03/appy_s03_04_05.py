#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:22:37 (UT+08:00) daisuke>
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
