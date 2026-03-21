#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/10/13 13:26:06 (UT+08:00) daisuke>
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
