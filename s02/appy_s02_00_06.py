#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 15:59:51 (UT+08:00) daisuke>
#

# importing os module
import os

# obtaining the value of environmental variable "LANG"
env_lang = os.environ['LANG']

# printing the value of environmental variable "LANG"
print (f'LANG = {env_lang}')
