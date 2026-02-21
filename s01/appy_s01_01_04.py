#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/02 21:14:57 (UT+08:00) daisuke>
#

# two numbers
a, b = 23, 7

# calculation
quotient  = a // b
remainder = a % b

# printing result of calculation
print (f'a         = {a}')
print (f'b         = {b}')
print (f'quotient  = {quotient}')
print (f'remainder = {remainder}')
print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')
