#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/10/13 13:21:10 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_K        = astropy.units.K
u_keV      = astropy.units.keV
u_T_energy = astropy.units.temperature_energy ()

# energy
energy = 1.0 * u_keV

# calculation of equivalent temperature for energy of 1 keV
T = energy.to (u_K, equivalencies=u_T_energy)

# printing result
print (f'energy = {energy:g}  ==>  temperature = {T:g}')
