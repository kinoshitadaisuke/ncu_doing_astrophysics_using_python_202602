#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:54:59 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# command to be executed
command = 'uname -srm'

# executing a command "uname" and capturing output
result = subprocess.run (command, shell=True, capture_output=True)

# stdout of command execution
output = result.stdout.decode ('utf-8')

# printing result of command execution
print (f'Outputs from the execution of command "{command}":')
print (f'{output}')
