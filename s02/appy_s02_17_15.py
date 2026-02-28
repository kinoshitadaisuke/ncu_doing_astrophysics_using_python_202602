#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/08 13:34:56 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.symbols ('x')

# function f(x)
f = x**4 * sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# integration of f(x) from 0 to infinity
I = sympy.integrate (f, (x, 0, pinf))

# printing result
print (f'I = {I}')
