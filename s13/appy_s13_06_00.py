#!/usr/pkg/bin/python3

#
# Time-stamp: <2025/12/02 09:27:10 (UT+08:00) daisuke>
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
descr  = "finding coordinates using name resolver"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
list_resolver = ['simbad', 'ned']
parser.add_argument ('-r', '--resolver', choices=list_resolver, \
                     default='simbad', help='choice of name resolver')
parser.add_argument ('-t', '--target', default='', help='target name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
name_resolver = args.resolver
target_name   = args.target

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
    
# printing coordinate
print (f'Target Name: {target_name}')
print (f'  RA:  {coord_ra_str} = {coord_ra_deg} deg')
print (f'  Dec: {coord_dec_str} = {coord_dec_deg} deg')
