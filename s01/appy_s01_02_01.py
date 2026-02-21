#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/02 21:15:52 (UT+08:00) daisuke>
#

# importing sys module
import sys

# reading an integer number from keyboard typing
a_str = input ('Type one integer number: ')

# converting a string into integer
try:
    a = int (a_str)
except:
    print (f'ERROR: failed to convert string "{a_str}" into integer!')
    sys.exit (1)

# if and else statements
if (a > 0):
    print ("The number you type is a positive number.")
elif (a < 0):
    print ("The number you type is a negative number.")
else:
    print ("The number you type is zero.")
