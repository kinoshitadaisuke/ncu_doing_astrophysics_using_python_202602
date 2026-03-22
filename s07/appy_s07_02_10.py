#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:54:54 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.table

# VOTable file
file_vot = 'exoplanet.vot'

# reading VOTable file and making an Astropy table
table_exoplanet = astropy.table.Table.read (file_vot)

# printing name, mass, semimajor axis, orbital period, detection type,
# and year of discovery of exoplanets
print (table_exoplanet["name", "mass", "semi_major_axis", \
                       "orbital_period", "detection_type", "discovered"])
