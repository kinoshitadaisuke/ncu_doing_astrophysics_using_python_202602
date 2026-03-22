#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:51:44 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# Solar luminosity
L_S = astropy.constants.L_sun

# printing Solar radius, Jupiter radius, and Earth radius
print (L_S, "\n")

# amount of 10,000 Solar luminosity
print (f'    1 L_S = {L_S:g}')
print (f'10000 L_S = {10000 * L_S:g}')
