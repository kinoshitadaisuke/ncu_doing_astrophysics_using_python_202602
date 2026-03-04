#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:27:38 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# output file name
file_output = 'numpy_04.npz'

# lists
list_c = [ -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0 ]
list_d = [
    [10.0, 20.0, 30.0],
    [40.0, 50.0, 60.0],
    [70.0, 80.0, 90.0],
]

# making Numpy arrays from lists
array_c = numpy.array (list_c)
array_d = numpy.array (list_d)

# printing Numpy arrays
print (f'array_c:')
print (f'{array_c}')
print (f'array_d:')
print (f'{array_d}')

# saving Numpy array into "npz" file
numpy.savez (file_output, array_c=array_c, array_d=array_d)
