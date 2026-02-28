#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 13:34:18 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = sympy.sqrt (4 - x**2)

# integration of f(x) from 0 to 2
I = sympy.integrate (f, (x, 0, 2))

# printing result
print (f'I = {I}')
