#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:00:00 (UT+08:00) daisuke>
#

# importing os module
import os

# getting the name of the operating system
os_info = os.uname ()

# printing system information
print (f'about this system:')
print (f'  architecture = {os_info.machine}')
print (f'  OS name      = {os_info.sysname}')
print (f'  version      = {os_info.release}')
