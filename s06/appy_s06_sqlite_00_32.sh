#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:50 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db \
	"select * from dwarfplanet where P > 300;"
