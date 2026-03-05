#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:23:41 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.logspace ()
a = numpy.logspace (-5.0, 5.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = numpy.log10 (a)

# printing b
print (f'b = log10 (a) = {b}')
