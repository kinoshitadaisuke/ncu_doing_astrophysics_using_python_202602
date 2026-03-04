#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:11:35 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.array ([5.0, 3.0, 7.0, 4.0, 9.0, 8.0, 1.0, 6.0, 2.0, 0.0])

# printing "a"
print (f'a:\n{a}')

# sorting by heap sort
b = numpy.sort (a, kind="heapsort")

# printing "b"
print (f'b = numpy.sort (a, kind="heapsort"):\n{b}')
