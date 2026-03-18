#!/bin/sh

#
# Time-stamp: <2025/10/03 13:33:11 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header planet0.db \
	".mode table" \
	"select name,mass,diameter,satellite,ring,magnetic_field from planet;"
