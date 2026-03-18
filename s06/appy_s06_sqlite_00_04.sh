#!/bin/sh

#
# Time-stamp: <2025/10/03 13:32:01 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 planet0.db ".schema --indent"
