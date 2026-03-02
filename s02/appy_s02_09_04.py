#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 21:19:44 (UT+08:00) daisuke>
#

# data file
file_data = 'planets_solsys.data'

# opening file for reading
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if the line starts with '#'
        if (line[0] == '#'):
            # then, skip
            continue
        # splitting the line into three fields
        (name, mass_str, diameter_str) = line.split ()
        # converting string into float
        try:
            mass = float (mass_str)
        except:
            continue
        try:
            diameter = float (diameter_str)
        except:
            continue
        # printing data
        print (f'{name}')
        print (f'  mass [kg]    : {mass:g}')
        print (f'  diameter [m] : {diameter:g}')
