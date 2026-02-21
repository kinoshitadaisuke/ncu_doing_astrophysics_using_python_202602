#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/02 21:16:12 (UT+08:00) daisuke>
#

# initialisation of a variable "total"
total = 0

# calculating 1 + 2 + 3 + ... + 10 using "for" statement
for i in range (1, 11, 1):
    # adding "i" to "total"
    total += i

# printing result of calculation
print (f'1 + 2 + 3 + ... + 8 + 9 + 10 = {total}')
