#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:52:28 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# directory name
dir_zone = '/usr/share/zoneinfo'

# making a pathlib object
path_zone = pathlib.Path (dir_zone)

# finding directory contents
list_files = path_zone.iterdir ()

# printing directory contents
print (f'directory contents of "{path_zone}":')
for filename in list_files:
    # printing file name
    print (f'  {filename}')
