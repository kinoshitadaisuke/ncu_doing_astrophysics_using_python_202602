#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:15:19 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
func = 1 / sympy.sqrt (1/x - 1)

# integration of f(x) from x=0 to x=1
I = sympy.integrate (func, (x, 0, 1))

# printing result
print (f'I = {I}')
