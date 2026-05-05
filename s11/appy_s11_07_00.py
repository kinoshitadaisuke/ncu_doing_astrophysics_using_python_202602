#!/usr/bin/env python3

#
# Time-stamp: <2026/05/05 12:14:19 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# construction of parser object for argparse
descr  = 'converting VOT file into text file'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', default='abc.vot.gz', \
                     help='input VOTable file name')
parser.add_argument ('-o', '--output', default='xyz.list', \
                     help='output file name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_votable = args.input
file_output  = args.output

# making pathlib object
path_votable = pathlib.Path (file_votable)
# existing check of input VOT file
if not path_votable.exists ():
    # printing a message
    print (f'ERROR:')
    print (f'ERROR: VOTable file "{file_votable}" does not exist!')
    print (f'ERROR:')
    # exit the program
    sys.exit (0)

# reading VOTable file
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['SOURCE_ID'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_rv        = numpy.array (table['radial_velocity'])
data_b         = numpy.array (table['phot_bp_mean_mag'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_r         = numpy.array (table['phot_rp_mean_mag'])
data_br        = numpy.array (table['bp_rp'])
data_bg        = numpy.array (table['bp_g'])
data_gr        = numpy.array (table['g_rp'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_ra_err    = numpy.array (table['ra_error'])
data_dec_err   = numpy.array (table['dec_error'])
data_pmra_err  = numpy.array (table['pmra_error'])
data_pmdec_err = numpy.array (table['pmdec_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = f'# star ID, RA, Dec, parallax, pmra, pmdec, radial velocity,' \
        + f' b mag, g mag, r mag, b-r, b-g, g-r, parallax SNR,' \
        + f' b mag SNR, g mag SNR, r mag SNR\n'
    fh.write (header)
    # for each star
    for i in range ( len (data_id) ):
        # writing data into file
        record = f"{data_id[i]:19d}" \
            + f" {data_ra[i]:10.6f} {data_dec[i]:+10.6f}" \
            + f" {data_parallax[i]:10.6f}" \
            + f" {data_pmra[i]:10.6f} {data_pmdec[i]:10.6f}" \
            + f" {data_rv[i]:+10.6f}" \
            + f" {data_b[i]:9.6f} {data_g[i]:9.6f} {data_r[i]:9.6f}" \
            + f" {data_br[i]:9.6f} {data_bg[i]:9.6f} {data_gr[i]:9.6f}" \
            + f" {data_p_snr[i]:9.6f}" \
            + f" {data_b_snr[i]:9.6f} {data_g_snr[i]:9.6f} {data_r_snr[i]:9.6f}\n"
        fh.write (record)
