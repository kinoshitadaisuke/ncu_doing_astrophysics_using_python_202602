#!/bin/sh

#
# Time-stamp: <2026/03/19 10:36:13 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 bsc5.db ".schema --indent"
