#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:07:40 (UT+08:00) daisuke>
#

# importing math module
import math

# two floats "a" and "b"
a = 12.34
b = -56.78

# modf
(a_fractional, a_integer) = math.modf (a)
(b_fractional, b_integer) = math.modf (b)

# printing results
print (f'Use of modf () function:')
print (f'  a                    = {a}')
print (f'  integer part of a    = {a_integer}')
print (f'  fractional part of a = {a_fractional}')
print (f'  b                    = {b}')
print (f'  integer part of b    = {b_integer}')
print (f'  fractional part of b = {b_fractional}')
print (f'')
