#!/usr/bin/env python3

#
# Time-stamp: <2026/03/01 18:35:14 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# compressed data file
file_numbers = 'numbers.data.gz'

# output data file
file_output = 'numbers.data'

# opening compressed file for reading
with gzip.open (file_numbers, 'rb') as fh_in:
    # reading file
    data_byte = fh_in.read ()

# decoding raw byte data into UTF-8 text
data_utf8 = data_byte.decode ('utf-8')

# opening file for writing
with open (file_output, 'w') as fh_out:
    # writing data into file
    fh_out.write (data_utf8)
