#!/usr/bin/env python3

#
# Time-stamp: <2026/03/03 10:10:51 (UT+08:00) daisuke>
#

# importing zipfile module
import zipfile

# zip file
file_zip = 'files2.zip'

# opening file for reading
with zipfile.ZipFile (file_zip, 'r') as fh:
    # extracting files
    fh.extractall ()
