#!/bin/sh

#
# Time-stamp: <2025/10/03 13:32:48 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header planet0.db "select * from planet;"
