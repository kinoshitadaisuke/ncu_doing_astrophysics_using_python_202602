#!/bin/sh

#
# Time-stamp: <2025/10/03 13:37:25 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 mpcorb.db ".schema --indent"
