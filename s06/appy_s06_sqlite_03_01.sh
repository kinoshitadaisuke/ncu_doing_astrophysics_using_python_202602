#!/bin/sh

#
# Time-stamp: <2025/10/03 13:37:01 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 hip.db ".schema --indent"
