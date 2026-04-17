#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/11/03 14:14:59 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('osc_0000_1989/*.json')

# printing file names
for file in sorted (files):
    print (file)
