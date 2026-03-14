#!/usr/bin/env python3

#
# Time-stamp: <2026/03/14 21:14:09 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}')
