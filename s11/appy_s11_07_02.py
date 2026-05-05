#!/usr/bin/env python3

#
# Time-stamp: <2026/05/05 12:48:48 (UT+08:00) daisuke>
#    

# importing argparse module
import argparse

# importing math module
import math

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'selecting stars by distance'
parser = argparse.ArgumentParser (description=descr)

parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-a', '--min', type=float, help='minimum distance value')
parser.add_argument ('-b', '--max', type=float, help='maximum distance value')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input  = args.input
file_output = args.output
dist_min    = args.min
dist_max    = args.max

# making empty lists for storing data
list_id       = []
list_ra       = []
list_dec      = []
list_parallax = []
list_pmra     = []
list_pmdec    = []
list_rv       = []
list_b        = []
list_g        = []
list_r        = []
list_br       = []
list_bg       = []
list_gr       = []
list_p_snr    = []
list_b_snr    = []
list_g_snr    = []
list_r_snr    = []

# opening input data file
with open (file_input, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (star_id, ra, dec, parallax, pmra, pmdec, rv, mag_b, mag_g, mag_r, \
         colour_br, colour_bg, colour_gr, p_snr, b_snr, g_snr, r_snr) \
         = line.split ()
        # converting string into float or int
        try:
            star_id = int (star_id)
        except:
            star_id = math.nan
        try:
            ra = float (ra)
        except:
            ra = math.nan
        try:
            dec = float (dec)
        except:
            dec = math.nan
        try:
            parallax = float (parallax)
        except:
            parallax = math.nan
        try:
            pmra = float (pmra)
        except:
            pmra = math.nan
        try:
            pmdec = float (pmdec)
        except:
            pmdec = math.nan
        try:
            rv = float (rv)
        except:
            rv = math.nan
        try:
            mag_b = float (mag_b)
        except:
            mag_b = math.nan
        try:
            mag_g = float (mag_g)
        except:
            mag_g = math.nan
        try:
            mag_r = float (mag_r)
        except:
            mag_r = math.nan
        try:
            colour_br = float (colour_br)
        except:
            colour_br = math.nan
        try:
            colour_bg = float (colour_bg)
        except:
            colour_bg = math.nan
        try:
            colour_gr = float (colour_gr)
        except:
            colour_gr = math.nan
        try:
            p_snr = float (p_snr)
        except:
            p_snr = math.nan
        try:
            b_snr = float (b_snr)
        except:
            b_snr = math.nan
        try:
            g_snr = float (g_snr)
        except:
            g_snr = math.nan
        try:
            r_snr = float (r_snr)
        except:
            r_snr = math.nan
        # appending data to lists
        list_id.append (star_id)
        list_ra.append (ra)
        list_dec.append (dec)
        list_parallax.append (parallax)
        list_pmra.append (pmra)
        list_pmdec.append (pmdec)
        list_rv.append (rv)
        list_b.append (mag_b)
        list_g.append (mag_g)
        list_r.append (mag_r)
        list_br.append (colour_br)
        list_bg.append (colour_bg)
        list_gr.append (colour_gr)
        list_p_snr.append (p_snr)
        list_b_snr.append (b_snr)
        list_g_snr.append (g_snr)
        list_r_snr.append (r_snr)

# converting list into numpy array
data_id       = numpy.array (list_id)
data_ra       = numpy.array (list_ra)
data_dec      = numpy.array (list_dec)
data_parallax = numpy.array (list_parallax)
data_pmra     = numpy.array (list_pmra)
data_pmdec    = numpy.array (list_pmdec)
data_rv       = numpy.array (list_rv)
data_b        = numpy.array (list_b)
data_g        = numpy.array (list_g)
data_r        = numpy.array (list_r)
data_br       = numpy.array (list_br)
data_bg       = numpy.array (list_bg)
data_gr       = numpy.array (list_gr)
data_p_snr    = numpy.array (list_p_snr)
data_b_snr    = numpy.array (list_b_snr)
data_g_snr    = numpy.array (list_g_snr)
data_r_snr    = numpy.array (list_r_snr)
        
# distance
data_distance = numpy.array ([])
for i in range ( len (data_parallax) ):
    # rejecting stars of negative parallax, no measurement of parallax,
    # and parallax SNR less than 10.0
    if ( (data_parallax[i] <= 0.0) or (numpy.isnan (data_parallax[i]) ) \
         or (data_p_snr[i] < 10.0) ):
        data_distance = numpy.append (data_distance, -1.0)
    else:
        data_distance = numpy.append (data_distance, 1000.0 / data_parallax[i])

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = f'# star ID, RA, Dec, parallax, pmra, pmdec, radial velocity' \
        + f' b mag, g mag, r mag, b-r, b-g, g-r\n'
    fh.write (header)
    # examining each star
    for i in range ( len (data_distance) ):
        # rejecting stars of low signal-to-noise ratio
        if (data_b_snr[i] < 10.0):
            continue
        if (data_g_snr[i] < 10.0):
            continue
        if (data_r_snr[i] < 10.0):
            continue
        # selecting stars between distances dist_min and dist_max
        if ( (data_distance[i] >= dist_min) \
             and (data_distance[i] <= dist_max) ):
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
