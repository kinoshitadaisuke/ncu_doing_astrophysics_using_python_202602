#!/usr/pkg/bin/python3

#
# Time-stamp: <2025/12/02 12:20:05 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing astroquery module
import astroquery.simbad
import astroquery.ipac.ned
import astroquery.mast

# importing astropy module
import astropy.coordinates
import astropy.units

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# constructing parser object
descr  = "downloading JWST image"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
list_resolver = ['simbad', 'ned']
parser.add_argument ('-r', '--resolver', choices=list_resolver, \
                     default='simbad', help='choice of name resolver')
parser.add_argument ('-t', '--target', default='', help='target name')
parser.add_argument ('-s', '--radius', type=float, default=0.1, \
                     help='radius of search area in degree')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
name_resolver = args.resolver
target_name   = args.target
radius_deg    = args.radius * u_deg

# checking target name
if (target_name == ''):
    # printing error message
    print ("No target name is given!")
    # exit
    sys.exit ()

# using name resolver
if (name_resolver == 'simbad'):
    query_result = astroquery.simbad.Simbad.query_object (target_name)
elif (name_resolver == 'ned'):
    query_result = astroquery.ipac.ned.Ned.query_object (target_name)

# RA and Dec
RA  = query_result['ra']
Dec = query_result['dec']

# coordinate
if (name_resolver == 'simbad'):
    coord = astropy.coordinates.SkyCoord (RA[0], Dec[0], unit=(u_deg, u_deg))
elif (name_resolver == 'ned'):
    coord = astropy.coordinates.SkyCoord (RA[0], Dec[0], unit=(u_deg, u_deg))

coord_str = coord.to_string (style='hmsdms')
(coord_ra_str, coord_dec_str) = coord_str.split ()
coord_ra_deg  = coord.ra.deg
coord_dec_deg = coord.dec.deg
coord_deg     = f'{coord_ra_deg} {coord_dec_deg}'
    
# printing coordinate
print (f'Target Name: {target_name}')
print (f'  RA:  {coord_ra_str} = {coord_ra_deg} deg')
print (f'  Dec: {coord_dec_str} = {coord_dec_deg} deg')

# JWST image search
obs_table \
    = astroquery.mast.Observations.query_criteria (coordinates=coord_deg, \
                                                   radius=radius_deg, \
                                                   obs_collection='JWST', \
                                                   dataproduct_type='image')

# printing result of the search
print (f'# ObsID, instrument, filter, exptime, calib level, target name')
for i in range (len (obs_table)):
    print (f'{obs_table[i]["obsid"]:9s}', \
           f'{obs_table[i]["instrument_name"]:12s}', \
           f'{obs_table[i]["filters"]:10s}', \
           f'{obs_table[i]["t_exptime"]:6.1f}', \
           f'{obs_table[i]["calib_level"]}', \
           f'{obs_table[i]["target_name"]}')
