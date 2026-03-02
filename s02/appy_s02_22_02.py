#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:13:26 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = (1 + 1/x)**x

# limit x --> infinity
lim_f = sympy.limit (f, x, sympy.oo)

# printing result
print (f'lim x->infty [{f}] = {lim_f}')
