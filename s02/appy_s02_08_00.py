#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:04:22 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# time offset from UTC
#   local time in Taiwan = UT + 8-hr
dt = datetime.timedelta (hours=8)

# current time in local time
time_now_local = datetime.datetime.now (tz=datetime.timezone (dt))

# printing result
print (f'current local time: {time_now_local}')
