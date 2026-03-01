#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 15:59:01 (UT+08:00) daisuke>
#

# importing os module
import os

# knowing where I am now
cwd = os.getcwd ()

# printing where I am now
print (f'currently working directory = "{cwd}"')

# target directory
dir_target = '/etc'

# printing status
print (f'now, changing directory to "{dir_target}"...')

# changing directory
os.chdir (dir_target)

# printing status
print (f'finished changing directory to "{dir_target}"!')

# knowing where I am now
cwd = os.getcwd ()

# printing where I am now
print (f'currently working directory = "{cwd}"')
