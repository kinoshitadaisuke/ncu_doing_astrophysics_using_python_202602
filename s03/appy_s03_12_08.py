#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/14 20:25:38 (UT+08:00) daisuke>
#

# input data file
file_input = 'numpy_02.data'

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading data in the file line-by-line
    for line in fh_in:
        # removing line feed at the end of the line
        line = line.rstrip ()
        # printing data
        print (f'{line}')
