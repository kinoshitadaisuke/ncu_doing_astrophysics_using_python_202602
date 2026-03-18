#!/bin/sh

#
# Time-stamp: <2025/10/03 13:36:57 (UT+08:00) daisuke>
#

# printing tables in the database file "hip.db"
sqlite3 hip.db ".tables"
