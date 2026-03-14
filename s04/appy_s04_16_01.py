#!/usr/bin/env python3

#
# Time-stamp: <2026/03/13 15:30:57 (UT+08:00) daisuke>
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

# output file
file_output = 'campus_map0.png'

# resolution of output file in DPI
resolution_dpi = 225.0

# opening and reading an image from a file
image = PIL.Image.open (file_jpeg)

# converting PIL Image object into Numpy array
array_image = numpy.asarray (image)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting image
ax.imshow (array_image)

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
