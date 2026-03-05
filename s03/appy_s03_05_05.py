#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:23:32 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a = numpy.linspace (0.0, 10.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = numpy.sqrt (a)

# printing b
print (f'b = sqrt (a)\n  = {b}')
