#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:50:57 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.01 * c

# object type of "c"
type_c = type (c)

# object type of "v"
type_v = type (v)

# printing object type of "c"
print (f'type of "c" = {type_c}')

# printing object type of "v"
print (f'type of "v" = {type_v}')
