#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 21:20:05 (UT+08:00) daisuke>
#

# importing csv module
import csv

# data file
file_data = 'planets_solsys.data'

# output csv file
file_csv = 'planets_solsys.csv'

# making an empty list for storing data
list_planets = []

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
        # storing data in a list
        list_planets.append ([name, mass, diameter])

# opening file for writing
with open (file_csv, 'w') as fh:
    # CSV writer
    csvwriter = csv.writer (fh, dialect='unix')
    # writing data
    for i in range (len (list_planets)):
        csvwriter.writerow (list_planets[i])
