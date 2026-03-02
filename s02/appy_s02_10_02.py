#!/usr/bin/env python3

#
# Time-stamp: <2026/03/01 11:15:30 (UT+08:00) daisuke>
#

# importing json module
import json

# json file
file_json = 'stars.json'

# new json file
file_json2 = 'stars2.json'

# opening file for reading
with open (file_json, 'r') as fh:
    # reading json file
    dic_data = json.load (fh)

# adding constellation information to data
for key1 in sorted (dic_data.keys ()):
    if (key1 == 'Sirius'):
        dic_data[key1]["constellation"] = "CMa"
    elif (key1 == 'Canopus'):
        dic_data[key1]["constellation"] = "Car"
    elif (key1 == 'Rigil Kentaurus'):
        dic_data[key1]["constellation"] = "Cen"
    elif (key1 == 'Arcturus'):
        dic_data[key1]["constellation"] = "Boo"
    elif (key1 == 'Vega'):
        dic_data[key1]["constellation"] = "Lyr"
    elif (key1 == 'Capella'):
        dic_data[key1]["constellation"] = "Aur"
    elif (key1 == 'Rigel'):
        dic_data[key1]["constellation"] = "Ori"
    elif (key1 == 'Procyon'):
        dic_data[key1]["constellation"] = "CMi"

# printing data
for key1 in sorted (dic_data.keys ()):
    print (f'{key1}')
    for key2 in sorted (dic_data[key1].keys ()):
        print (f'  {key2} : {dic_data[key1][key2]}')

# opening file for writing
with open (file_json2, 'w') as fh:
    # writing json file
    json.dump (dic_data, fh, indent=4)
