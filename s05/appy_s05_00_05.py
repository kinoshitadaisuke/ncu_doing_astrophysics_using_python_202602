#!/usr/bin/env python3

#
# Time-stamp: <2026/03/14 21:14:28 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}:')
    print (f'  value = {scipy.constants.value (constant)}')
    print (f'  error = {scipy.constants.precision (constant)}')
    print (f'  unit  = {scipy.constants.unit (constant)}')
