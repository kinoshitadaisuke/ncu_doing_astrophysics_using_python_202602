#!/usr/bin/env python3

#
# Time-stamp: <2026/04/20 08:41:52 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('osc_0000_1989/*.json')

# printing file names
for file in sorted (files):
    print (file)
