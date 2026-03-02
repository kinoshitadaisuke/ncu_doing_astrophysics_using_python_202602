#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:14:03 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = x**2

# integration of f(x)
I = sympy.integrate (f, x)

# printing result
print (f'f(x)  = {f}')
print (f'integration of f(x) = {I}')
