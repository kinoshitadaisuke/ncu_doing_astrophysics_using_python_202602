#!/usr/bin/env python3

#
# Time-stamp: <2026/03/14 18:47:37 (UT+08:00) daisuke>
#

# importing math module
import math

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# output file
file_output = 'appy_s04_17_00.png'

# resolution of output file in DPI
resolution_dpi = 225.0

# empty lists for storing data
list_x = []
list_y = []
list_u = []
list_v = []

# generating data
for r in range (1, 20, 2):
    theta = 0.0
    while (theta < 360.0):
        # position (x, y) and vector (u, v)
        x = r * math.cos (theta * math.pi / 180.0)
        y = r * math.sin (theta * math.pi / 180.0)
        u = 0.001 * math.cos (theta * math.pi / 180.0)
        v = 0.001 * math.sin (theta * math.pi / 180.0)
        # appending data to lists
        list_x.append (x)
        list_y.append (y)
        list_u.append (u)
        list_v.append (v)
        # adding 22.5 to theta
        theta += 22.5

# making numpy arrays
array_x = numpy.array (list_x)
array_y = numpy.array (list_y)
array_u = numpy.array (list_u)
array_v = numpy.array (list_v)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# settings for axes
ax.set_aspect('equal', 'box')
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-10.0, +10.0)

# plotting data
ax.quiver (array_x, array_y, array_u, array_v, color='blue')

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
