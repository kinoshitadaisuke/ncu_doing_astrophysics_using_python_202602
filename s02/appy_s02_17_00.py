#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:13:11 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = (x + 1)**2

# expansion of (x+1)**2
f2 = sympy.expand (f)

# printing result
print (f'{f} = {f2}')
