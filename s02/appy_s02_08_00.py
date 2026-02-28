#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:59:53 (UT+08:00) daisuke>
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
