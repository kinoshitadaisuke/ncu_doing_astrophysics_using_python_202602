#!/usr/bin/env python3

#
# Time-stamp: <2026/02/28 16:14:32 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.symbols ('x')

# function y(x)
y = sympy.Function ('y')

# Lane-Emden equation of n=0
lane_emden_n0 = sympy.Eq (x**-2 * (x**2 * y(x).diff (x)).diff (x), -1)

# printing equation
print (f'equation: {lane_emden_n0}')

# solving Lane-Emden equation of n=0
sol = sympy.dsolve (lane_emden_n0, y(x))

# printing result
print (f'solution: {sol}')
