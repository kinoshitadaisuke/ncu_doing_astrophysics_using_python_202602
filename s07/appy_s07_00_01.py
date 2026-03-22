#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:50:50 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.01 * c

# printing c and v
print (f'c = {c}')
print (f'v = 0.01 * {c}')
print (f'  = {v}')
