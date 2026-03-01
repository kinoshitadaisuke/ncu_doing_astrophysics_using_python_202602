#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:13:18 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = x**2 + x - 2

# factorisation of f
f2 = sympy.factor (f)

# printing result
print (f'{f} = {f2}')
