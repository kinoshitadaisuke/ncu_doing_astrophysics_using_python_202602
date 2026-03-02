#!/usr/bin/env python3

#
# Time-stamp: <2026/03/02 22:17:08 (UT+08:00) daisuke>
#

# importing tarfile module
import tarfile

# tar file
file_tar = 'files.tar'

# opening file for reading
with tarfile.open (file_tar, 'r:*') as fh:
    # extracting files
    fh.extractall ()
