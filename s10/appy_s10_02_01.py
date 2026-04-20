#!/usr/bin/env python3

#
# Time-stamp: <2026/04/20 08:38:46 (UT+08:00) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanets/data/exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing type of data
print (f'type (data)    = {type (data)}')

# printing type of data[0]
print (f'type (data[0]) = {type (data[0])}')
