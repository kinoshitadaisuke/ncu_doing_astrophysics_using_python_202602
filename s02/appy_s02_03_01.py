#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:01:53 (UT+08:00) daisuke>
#

# input file name
file_input = 'pi_1000.txt'

# opening file for reading
with open (file_input, 'r') as fh_read:
    # reading file line-by-line
    for line in fh_read:
        # printing line
        print (f'{line}', end='')
