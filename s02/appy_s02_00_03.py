#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 15:59:19 (UT+08:00) daisuke>
#

# importing os module
import os

# target directory
dir_target = '/bin'

# obtaining a list of files and directories at the directory "dir_target"
list_files = os.listdir (path=dir_target)

# printing files and directories
print (f'list of files and directories at "{dir_target}":')
# for each file (or directory) in the list
for filename in list_files:
    # printing name of file (or directory)
    print (f'  {filename}')
