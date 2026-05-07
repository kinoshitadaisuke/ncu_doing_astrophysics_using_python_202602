#!/usr/bin/env python3

#
# Time-stamp: <2026/05/07 17:18:11 (UT+08:00) daisuke>
#

# importing tarfile module
import tarfile

# gzipped tar file
file_targz = 'linear.tar.gz'

# target directory for extraction of files
dir_target = 'linear'

# opening tar file
with tarfile.open (file_targz, 'r:gz') as fh_targz:
    # extracting files
    fh_targz.extractall (path=dir_target)
