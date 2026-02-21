#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/02 21:16:02 (UT+08:00) daisuke>
#

# initialisation of a variable "total"
total = 0

# data
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# calculating 1 + 2 + 3 + ... + 10 using "for" statement
for i in list_data:
    # adding "i" to "total"
    total = total + i

# printing result of calculation
print (f'1 + 2 + 3 + ... + 8 + 9 + 10 = {total}')
