#!/bin/sh

#
# Time-stamp: <2025/10/03 13:33:25 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header -column planet0.db \
	"select name,mass,diameter,satellite,ring,magnetic_field from planet \
	where satellite >= 10;"
