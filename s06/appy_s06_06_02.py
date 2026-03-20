#!/usr/bin/env python3

#
# Time-stamp: <2026/03/20 13:41:23 (UT+08:00) daisuke>
#

# data file
file_data = 'landolt_2009.data'

# opening file for reading
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # star name
        star_name = line[0:11].strip ()
        # right ascension
        ra_h = line[12:14]
        ra_m = line[15:17]
        ra_s = line[18:24]
        ra   = f'{ra_h}:{ra_m}:{ra_s}'
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
        # printing extracted data
        print (f'"{star_name}"')
        print (f'  RA     = "{ra}" = {ra_deg} deg')
        print (f'  Dec    = "{dec}" = {dec_deg} deg')
        print (f'  Vmag   = {mag_v}')
        print (f'  B-V    = {colour_bv}')
        print (f'  U-B    = {colour_ub}')
        print (f'  V-R    = {colour_vr}')
        print (f'  R-I    = {colour_ri}')
        print (f'  V-I    = {colour_vi}')
        print (f'  nobs   = {nobs}')
        print (f'  nnight = {nnight}')
