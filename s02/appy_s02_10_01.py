#!/usr/bin/env python3

#
# Time-stamp: <2026/03/01 11:07:40 (UT+08:00) daisuke>
#

# importing json module
import json

# json file
file_json = 'stars.json'

# opening file for reading
with open (file_json, 'r') as fh:
    # reading json file
    dic_data = json.load (fh)

# printing data
for key1 in sorted (dic_data.keys ()):
    print (f'{key1}')
    for key2 in sorted (dic_data[key1].keys ()):
        print (f'  {key2} : {dic_data[key1][key2]}')
