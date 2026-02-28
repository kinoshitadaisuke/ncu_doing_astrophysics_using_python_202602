#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 12:47:33 (UT+08:00) daisuke>
#

# importing sys module
import sys

while (True):
    # receiving an integer from keyboard input
    number_str = input ('Input an integer: ')
    # conversion from string into integer
    try:
        number = int (number_str)
    except:
        # printing message
        print (f'"{number_str}" is not a number!')
        # skipping current iteration
        continue
    # if the integer is greater than zero, then receive the other integer
    if (number > 0):
        # skipping current iteration
        continue
    # if the integer is equal to zero or less than zero, then stop the script
    else:
        # exit Python interpreter using sys.exit ()
        sys.exit (0)
