#!/bin/sh

#
# Time-stamp: <2025/10/03 13:34:15 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db \
	"select name, a, e, i, H from dwarfplanet order by H;"
