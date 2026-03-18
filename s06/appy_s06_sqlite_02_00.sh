#!/bin/sh

#
# Time-stamp: <2025/10/03 13:36:19 (UT+08:00) daisuke>
#

# making a database
sqlite3 bsc5.db ".read bsc5_makedb.sql"
