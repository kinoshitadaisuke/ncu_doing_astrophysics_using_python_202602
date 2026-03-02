#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:15:00 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# negative infinity
ninf = -sympy.oo

# integration of f(x)
I = sympy.integrate (f, (x, ninf, pinf))

# printing result
print (f'I = {I}')
