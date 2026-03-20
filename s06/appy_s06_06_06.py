#!/usr/bin/env python3

#
# Time-stamp: <2026/03/20 13:54:55 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# data file
file_data = 'landolt_2009.data'

# database file
file_db = 'landolt_2009.db'

# making an empty dictionary for storing data
dic_star = {}

# opening file for reading
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # star name
        star_name = line[0:11].strip ()
        # right ascension
        ra_h   = line[12:14]
        ra_m   = line[15:17]
        ra_s   = line[18:24]
        ra     = f'{ra_h}:{ra_m}:{ra_s}'
        ra_deg = (float (ra_h) + float (ra_m) / 60.0 + float (ra_s) / 3600.0) * 15.0
        # declination
        dec_sgn = line[25]
        dec_d   = line[26:28]
        dec_m   = line[29:31]
        dec_s   = line[32:37]
        dec     = f'{dec_sgn}{dec_d}:{dec_m}:{dec_s}'
        if (dec_sgn == '-'):
            dec_deg = (float (dec_d) + float (dec_m) / 60.0 + float (dec_s) / 3600.0) * -1.0
        else:
            dec_deg = float (dec_d) + float (dec_m) / 60.0 + float (dec_s) / 3600.0
        # V band magnitude
        try:
            mag_v = float (line[38:44])
        except:
            mag_v = +999.9
        # B-V colour index
        try:
            colour_bv = float (line[45:51])
        except:
            colour_bv = +999.9
        # U-B colour index
        try:
            colour_ub = float (line[52:58])
        except:
            colour_ub = +999.9
        # V-R colour index
        try:
            colour_vr = float (line[59:65])
        except:
            colour_vr = +999.9
        # R-I colour index
        try:
            colour_ri = float (line[66:72])
        except:
            colour_ri = +999.9
        # V-I colour index
        try:
            colour_vi = float (line[73:79])
        except:
            colour_vi = +999.9
        # number of observations
        try:
            nobs = int (line[80:83])
        except:
            nobs = -999
        # number of nights observed
        try:
            nnight = int (line[84:87])
        except:
            nnight = -999
        # adding data into dictionary
        if not (star_name in dic_star):
            dic_star[star_name] = {}
            dic_star[star_name]['RA']      = ra
            dic_star[star_name]['Dec']     = dec
            dic_star[star_name]['RA_deg']  = ra_deg
            dic_star[star_name]['Dec_deg'] = dec_deg
            dic_star[star_name]['Vmag']    = mag_v
            dic_star[star_name]['B-V']     = colour_bv
            dic_star[star_name]['U-B']     = colour_ub
            dic_star[star_name]['V-R']     = colour_vr
            dic_star[star_name]['R-I']     = colour_ri
            dic_star[star_name]['V-I']     = colour_vi
            dic_star[star_name]['nobs']    = nobs
            dic_star[star_name]['nnight']  = nnight

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # for each star
    for star in dic_star.keys ():
        # data
        ra      = dic_star[star]['RA']
        dec     = dic_star[star]['Dec']
        ra_deg  = dic_star[star]['RA_deg']
        dec_deg = dic_star[star]['Dec_deg']
        v       = dic_star[star]['Vmag']
        bv      = dic_star[star]['B-V']
        ub      = dic_star[star]['U-B']
        vr      = dic_star[star]['V-R']
        ri      = dic_star[star]['R-I']
        vi      = dic_star[star]['V-I']
        nobs    = dic_star[star]['nobs']
        nnight  = dic_star[star]['nnight']
        # SQL command to add data to table
        sql_adddata = f"INSERT INTO landolt VALUES ('{star}', '{ra}', '{dec}', {ra_deg}, {dec_deg}, {v}, {bv}, {ub}, {vr}, {ri}, {vi}, {nobs}, {nnight});"
        # executing SQL command to add data into table
        connection.sql (sql_adddata)
