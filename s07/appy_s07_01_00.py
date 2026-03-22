#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:51:56 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# a quantity object of 900.0 sec
t = 900.0 * u_sec

# printing t
print (f't = {t}')
