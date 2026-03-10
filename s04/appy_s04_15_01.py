#!/usr/bin/env python3

#
# Time-stamp: <2026/03/10 20:25:08 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# input FITS file name
file_fits = 'hltau_alma.fits'

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # printing basic information of FITS file
    print (hdu_list.info ())
    # reading FITS header, WCS information, and image data
    image  = hdu_list[0].data
    # printing image data
    print (f'shape of image data')
    print (f'  ndim  = {image.ndim}')
    print (f'  shape = {image.shape}')
    print (f'image data:')
    print (image)
