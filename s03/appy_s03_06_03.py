#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:25:28 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.array ([ [0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0], \
                   [8.0, 9.0, 10.0, 11.0], [12.0, 13.0, 14.0, 15.0] ])

# printing A
print (f'a:\n{a}')

# accessing to an element by indexing
print (f'a[0:2,1:3]:\n{a[0:2,1:3]}')
print (f'a[1:3,:]:\n{a[1:3,:]}')
print (f'a[:,1:3]:\n{a[:,1:3]}')
