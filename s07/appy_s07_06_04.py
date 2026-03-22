#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:59:04 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits

# input file name
file_input = 'm3.fits'

# opening FITS file
with astropy.io.fits.open (file_input) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())
