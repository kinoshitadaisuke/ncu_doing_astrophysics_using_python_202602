#!/bin/sh

#
# Time-stamp: <2026/03/19 10:37:19 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 ngc2000.db ".schema --indent"
