#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:37 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db \
	"select name, a, e, i, H from dwarfplanet order by H;"
