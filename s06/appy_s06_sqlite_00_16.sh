#!/bin/sh

#
# Time-stamp: <2026/03/19 10:33:36 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header -column planet0.db \
	"select name,mass,diameter,satellite from planet;"
