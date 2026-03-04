#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:04:23 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a = numpy.linspace (0.0, 10.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = a**2

# printing b
print (f'b = a**2 = {b}')
