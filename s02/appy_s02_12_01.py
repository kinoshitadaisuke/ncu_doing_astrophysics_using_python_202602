#!/usr/bin/env python3

#
# Time-stamp: <2026/03/02 22:12:29 (UT+08:00) daisuke>
#

# importing tarfile module
import tarfile

# tar file
file_tar = 'files.tar'

# opening file for reading
with tarfile.open (file_tar, 'r:*') as fh:
    # getting file names in tar file
    list_files = fh.getnames ()

# for each file name in list
for filename in list_files:
    # printing file name
    print (filename)
