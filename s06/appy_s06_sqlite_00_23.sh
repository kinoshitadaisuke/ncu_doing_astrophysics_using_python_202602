#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:08 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header -column planet0.db \
	"select name,mass,diameter,satellite,ring,magnetic_field from planet \
	where mass > 1e+26 and diameter > 50000;"
