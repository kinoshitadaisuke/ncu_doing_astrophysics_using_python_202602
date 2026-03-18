#!/bin/sh

#
# Time-stamp: <2025/10/03 13:36:26 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 bsc5.db ".schema --indent"
