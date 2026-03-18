#!/bin/sh

#
# Time-stamp: <2025/10/03 13:35:19 (UT+08:00) daisuke>
#

# importing data from CSV file
sqlite3 element.db ".import --csv --skip 1 periodictable.csv element"
