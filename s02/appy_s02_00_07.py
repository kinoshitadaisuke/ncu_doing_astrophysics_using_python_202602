#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:44:46 (UT+08:00) daisuke>
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
