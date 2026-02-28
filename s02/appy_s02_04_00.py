#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:51:55 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# file name
file_hosts = '/etc/hosts'

# making a pathlib object
path_hosts = pathlib.Path (file_hosts)

# existence check
if (path_hosts.exists ()):
    print (f'The file "{path_hosts}" exists!')
else:
    print (f'The file "{path_hosts}" DOES NOT exist!')
