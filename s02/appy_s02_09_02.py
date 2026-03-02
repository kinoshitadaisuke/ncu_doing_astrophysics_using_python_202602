#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 21:18:55 (UT+08:00) daisuke>
#

# importing csv module
import csv

# CSV file name
file_csv = 'stars.csv'

# opening file for reading
with open (file_csv, 'r') as fh:
    data_elements = csv.DictReader (fh)
    # printing data
    for line in data_elements:
        print (f'{line["spectral type"]}')
        print (f'  temperature [K]               : {line["temperature [K]"]}')
        print (f'  absolute magnitude            : {line["absolute magnitude"]}')
        print (f'  luminosity [solar luminosity] : {line["luminosity [solar luminosity]"]}')
