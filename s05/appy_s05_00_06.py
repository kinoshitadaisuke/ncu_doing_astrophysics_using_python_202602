#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/30 20:49:08 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# some units for length
angstrom = scipy.constants.angstrom
au       = scipy.constants.au
ly       = scipy.constants.light_year
parsec   = scipy.constants.parsec

# printing units for length
print (f'1 angstrom = {angstrom:g} [m]')
print (f'1 au       = {au:g} [m]')
print (f'1 ly       = {ly:g} [m]')
print (f'1 parsec   = {parsec:g} [m]')
