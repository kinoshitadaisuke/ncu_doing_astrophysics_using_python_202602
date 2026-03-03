#!/usr/bin/env python3

#
# Time-stamp: <2026/03/03 10:07:13 (UT+08:00) daisuke>
#

# importing zipfile module
import zipfile

# zip file
file_zip = 'files2.zip'

# opening file for reading
with zipfile.ZipFile (file_zip, 'r') as fh:
    # list of files in zip file
    list_files = fh.namelist ()

# printing list of files in zip file
for filename in list_files:
    # printing file name
    print (f'{filename}')
