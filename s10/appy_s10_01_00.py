#!/usr/bin/env python3

#
# Time-stamp: <2026/04/20 08:37:23 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# URL of GitHub repository
url_repo = 'https://github.com/architecture-building-systems/honey-badger.git'

# command for downloading GitHub repository
command_git = f'git clone {url_repo}'

# downloading GitHub repository
subprocess.run (command_git, shell=True)
