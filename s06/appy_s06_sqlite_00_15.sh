#!/bin/sh

#
# Time-stamp: <2026/03/19 10:33:25 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header planet0.db \
	"select name,mass,diameter,satellite from planet;"
