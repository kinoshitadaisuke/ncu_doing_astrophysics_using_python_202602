#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:12:35 (UT+08:00) daisuke>
#

# importing pint module
import pint

# units
ur       = pint.UnitRegistry ()
u_arcsec = ur.arcsec
u_mas    = ur.mas
u_pc     = ur.pc
u_au     = ur.au
u_m      = ur.metre

# parallax of Sirius
parallax = 374.5 * u_mas

# distance to Sirius
distance = 1.0 / parallax.to (u_arcsec) * u_pc * u_arcsec

# printing results
print (f'distance to Sirius = {distance}')
print (f'                   = {distance.to (u_au)}')
print (f'                   = {distance.to (u_m)}')
