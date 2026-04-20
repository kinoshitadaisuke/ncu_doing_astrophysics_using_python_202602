#!/usr/bin/env python3

#
# Time-stamp: <2026/04/20 08:37:45 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'honey-badger/examples/planets/planets.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing the column for mean temperature
print (f'{table["Planet", "Mean Temperature (C)"]}')
