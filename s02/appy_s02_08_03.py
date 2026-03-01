#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:05:46 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# timezone information (UT+0)
tzinfo = datetime.timezone (datetime.timedelta (0.0), name='UT+0')

# current time in UTC
time_now_utc = datetime.datetime.now (tz=tzinfo)

# printing result
print (f'current time in UTC = {time_now_utc}')
