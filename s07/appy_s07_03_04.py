#!/usr/bin/env python3

#
# Time-stamp: <2026/03/22 12:55:54 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# getting current date/time
now = astropy.time.Time.now ()

# date/time of J2000
j2000 = astropy.time.Time ('2000-01-01 12:00:00', format='iso', scale='utc')

# time between J2000 and now
delta_t = now - j2000

# printing date/time
print (f'j2000       = {j2000}')
print (f'now         = {now}')
print (f'now - j2000 = {delta_t} day = {delta_t.sec:g} sec')
