#!/usr/bin/env python3

#
# Time-stamp: <2026/03/13 13:55:15 (UT+08:00) daisuke>
#

# importing PIL module
import PIL

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# JPEG file
file_jpeg = 'campus_map.jpg'

# opening and reading an image from a file
image = PIL.Image.open (file_jpeg)

# converting PIL Image object into Numpy array
array_image = numpy.asarray (image)

# printing basic information about Numpy array
print (f'ndim     = {array_image.ndim}')
print (f'shape    = {array_image.shape}')
print (f'size     = {array_image.size}')
print (f'dtype    = {array_image.dtype}')
print (f'itemsize = {array_image.itemsize}')
