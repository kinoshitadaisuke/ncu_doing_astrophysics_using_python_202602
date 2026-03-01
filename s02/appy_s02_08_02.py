#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:05:39 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# current time in UTC
time_now_utc = datetime.datetime.now (tz=datetime.timezone.utc)

# printing result
print (f'current time in UTC = {time_now_utc}')
