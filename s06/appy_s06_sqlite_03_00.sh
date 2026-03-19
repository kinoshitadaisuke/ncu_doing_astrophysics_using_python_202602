#!/bin/sh

#
# Time-stamp: <2026/03/19 10:36:36 (UT+08:00) daisuke>
#

# printing tables in the database file "hip.db"
sqlite3 hip.db ".tables"
