#!/bin/sh

#
# Time-stamp: <2026/03/19 10:36:08 (UT+08:00) daisuke>
#

# making a database
sqlite3 bsc5.db ".read bsc5_makedb.sql"
