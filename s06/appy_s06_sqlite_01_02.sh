#!/bin/sh

#
# Time-stamp: <2026/03/19 10:35:48 (UT+08:00) daisuke>
#

# importing data from CSV file
sqlite3 element.db ".import --csv --skip 1 periodictable.csv element"
