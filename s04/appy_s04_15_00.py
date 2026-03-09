#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/23 07:50:54 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits

# input FITS file name
file_fits = 'hltau_alma.fits'

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # printing basic information of FITS file
    print (hdu_list.info ())
