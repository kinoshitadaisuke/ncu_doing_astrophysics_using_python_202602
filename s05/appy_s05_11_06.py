#!/usr/bin/env python3

#
# Time-stamp: <2026/03/17 13:29:48 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# output data file
file_output = 'appy_s05_11_06.data'

# pi
pi = numpy.pi

# amplitude
A0 = 9.8
A1 = 7.6
A2 = 5.4
A3 = 3.2

# frequency in Hz
f0 = 37.0
f1 = 43.0
f2 = 59.0
f3 = 71.0

# initial phase
delta0 = 0.2 * pi
delta1 = 0.5 * pi
delta2 = 0.7 * pi
delta3 = 0.9 * pi

# baseline
b = 30.0

# number of data points
n = 32768

# data acquisition interval in sec
dt = 0.0007

# time
t = numpy.linspace (0.0, n * dt, n, endpoint=False)

# synthetic data for FFT
y = A0 * numpy.sin (2.0 * pi * f0 * t - delta0) \
    + A1 * numpy.sin (2.0 * pi * f1 * t - delta1) \
    + A2 * numpy.sin (2.0 * pi * f2 * t - delta2) \
    + A3 * numpy.sin (2.0 * pi * f3 * t - delta3) \
    + b

# opening file for writing
with open (file_output, 'w') as fh:
    # for all the data
    for i in range (n):
        # writing data into file
        fh.write (f'{t[i]:12.6f}  {y[i]:12.9f}\n')
