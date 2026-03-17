#!/usr/bin/env python3

#
# Time-stamp: <2026/03/17 09:54:08 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# output data file
file_output = 'appy_s05_11_03.data'

# pi
pi = numpy.pi

# amplitude
A0 = 2.0
A1 = 1.7
A2 = 1.3

# frequency in Hz
f0 = 13.0
f1 = 19.0
f2 = 23.0

# initial phase
delta0 = 0.5 * pi
delta1 = 0.7 * pi
delta2 = 1.1 * pi

# baseline
b = 3.0

# number of data points
n = 8192

# data acquisition interval in sec
dt = 0.001

# time
t = numpy.linspace (0.0, n * dt, n, endpoint=False)

# synthetic data for FFT
y = A0 * numpy.sin (2.0 * pi * f0 * t - delta0) \
    + A1 * numpy.sin (2.0 * pi * f1 * t - delta1) \
    + A2 * numpy.sin (2.0 * pi * f2 * t - delta2) \
    + b

# opening file for writing
with open (file_output, 'w') as fh:
    # for all the data
    for i in range (n):
        # writing data into file
        fh.write (f'{t[i]:12.6f}  {y[i]:12.9f}\n')
