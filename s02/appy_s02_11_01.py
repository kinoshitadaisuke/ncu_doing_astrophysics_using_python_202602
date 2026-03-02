#!/usr/bin/env python3

#
# Time-stamp: <2026/03/01 17:47:24 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# compressed data file
file_numbers = 'numbers.data.gz'

# opening compressed file for reading
with gzip.open (file_numbers, 'rb') as fh_in:
    # reading file
    data_byte = fh_in.read ()

# decoding raw byte data into UTF-8 text
data_utf8 = data_byte.decode ('utf-8')

# printing data
print (data_utf8)
