#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 13:01:39 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# file of Yale Bright Star Catalogue
file_bsc = 'catalog.gz'

# making pathlib object
path_bsc = pathlib.Path (file_bsc)

# existence check of file
if (path_bsc.exists ()):
    print (f'File "{file_bsc}" exists.')
    print (f'Downloading of Yale Bright Star Catalogue was successfully done!')
else:
    print (f'File "{file_bsc}" DOES NOT exist.')
    print (f'Download Yale Bright Star Catalogue!')
