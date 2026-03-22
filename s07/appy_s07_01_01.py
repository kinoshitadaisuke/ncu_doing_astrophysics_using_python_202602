#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:52:03 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# a quantity object of 900.0 sec
t = 900.0 * u_sec

# value of t
t_value = t.value

# unit of t
t_unit = t.unit

# printing t, value of t, and unit of t
print (f't          = {t}')
print (f'value of t = {t_value}')
print (f'unit of t  = {t_unit}')
