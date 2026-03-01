#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:13:56 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = sympy.log (x)

# differentiation of f(x)
df_dx = sympy.diff (f, x)

# printing result
print (f'f(x)  = {f}')
print (f'df/dx = {df_dx}')
