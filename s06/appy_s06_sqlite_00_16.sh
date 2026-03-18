#!/bin/sh

#
# Time-stamp: <2025/10/03 13:32:59 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header -column planet0.db \
	"select name,mass,diameter,satellite from planet;"
