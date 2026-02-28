#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:52:12 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# file name
file_resolv = '/etc/resolv.conf'

# making a pathlib object
path_resolv = pathlib.Path (file_resolv)

# printing parent, name, suffix, stem
print (f'parent, name, suffix, and stem of "{path_resolv}":')
print (f'  parent of "{path_resolv}" = "{path_resolv.parent}"')
print (f'  name of "{path_resolv}"   = "{path_resolv.name}"')
print (f'  suffix of "{path_resolv}" = "{path_resolv.suffix}"')
print (f'  stem of "{path_resolv}"   = "{path_resolv.stem}"')
