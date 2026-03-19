#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:45 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db \
	"select name, a, e, i, perihelion, aphelion from dwarfplanet \
	order by aphelion desc;"
