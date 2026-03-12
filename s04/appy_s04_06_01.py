#!/usr/bin/env python3

#
# Time-stamp: <2026/03/12 11:23:57 (UT+08:00) daisuke>
#

# input data file
file_input = 'alf_ori.data'

# opening input file
with open (file_input, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # splitting data
        (date, mag_str, error_str, band, telescope) = line.split ()
        # conversion from string to float
        mag       = float (mag_str)
        mag_error = float (error_str)
        # printing data
        print (f'{date} {mag:6.3f} {mag_error:6.3f} {band} {telescope}')
