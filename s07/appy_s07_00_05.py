#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/10/13 13:12:05 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# astronomical unit
au = astropy.constants.au

# printing au
print (au, "\n")

# parsec
pc = astropy.constants.pc

# km/s
unit_km = astropy.units.km

# printing pc
print (pc, "\n")

# 1 au
print (f'1 au = {au:g}')
print (f'     = {au.to (unit_km):g}')

# 1 pc
print (f'1 pc = {pc:g}')
print (f'     = {pc / au} au')
