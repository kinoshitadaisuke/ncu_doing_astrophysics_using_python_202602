#!/usr/bin/env python3

#
# Time-stamp: <2026/03/04 16:30:13 (UT+08:00) daisuke>
#

# input data file
file_input = 'numpy_00.data'

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading data in the file line-by-line
    for line in fh_in:
        # removing line feed at the end of the line
        line = line.strip ()
        # printing data
        print (f'{line}')
