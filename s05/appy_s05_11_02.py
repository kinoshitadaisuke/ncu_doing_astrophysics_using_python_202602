#!/usr/bin/env python3

#
# Time-stamp: <2026/03/17 09:49:18 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.fft

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data file name
file_input = 'appy_s05_11_00.data'

# output file name
file_output = 'appy_s05_11_02.png'

# resolution in DPI
resolution_dpi = 150

# making empty lists for storing data
list_t = []
list_y = []

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # splitting line
        (t_str, y_str) = line.split ()
        # converting string into float
        t = float (t_str)
        y = float (y_str)
        # appending data to lists
        list_t.append (t)
        list_y.append (y)

# making numpy arrays
array_t = numpy.array (list_t)
array_y = numpy.array (list_y)

# data acquisition interval in sec
dt = array_t[1] - array_t[0]

#
# FFT
#

# frequency
array_f  = scipy.fft.fftfreq (array_y.size, dt)
# power
array_pc = scipy.fft.fft (array_y)
array_p  = 2.0 / array_pc.size * numpy.abs (array_pc)

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# axes
ax.set_xlabel ('Frequency [Hz]')
ax.set_ylabel ('Power')
ax.set_xlim (0.0, 30.0)

# plotting data
ax.plot (array_f[1:array_f.size // 2], array_p[1:array_p.size // 2], \
         linestyle='-', linewidth=2, color='blue', \
         label='power spectrum')

# legend
ax.legend ()

# saving plot into file
fig.savefig (file_output, dpi=resolution_dpi)
