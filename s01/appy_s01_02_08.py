#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/02 21:16:26 (UT+08:00) daisuke>
#

# printing odd number between 0 and 30
for i in range (30):
    # if number is divisible by 2, then skipping to next number
    if (i % 2 == 0):
        continue
    # if not, then it is an odd number
    print (f'{i} is an odd number.')
