#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:05:56 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays
a = numpy.array ([ [1.0, 2.0], [3.0, 4.0] ])
b = numpy.array ([ [5.0, 6.0], [7.0, 8.0] ])

# printing a and b
print (f'a:\n{a}')
print (f'b:\n{b}')

# calculation
# no need of using "for"
c = a + b

# printing c
print (f'c = a + b:\n{c}')
