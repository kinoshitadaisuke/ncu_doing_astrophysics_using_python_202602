#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:29 (UT+08:00) daisuke>
#

# creating a table
sqlite3 dwarf_planet2.db \
	"create table dwarfplanet2 (name text primary key, \
	a real, e real, i real, perihelion real, aphelion real, P real, H real);"

# importing data from a CSV file
sqlite3 dwarf_planet2.db \
	".import --csv '| grep -v \# dwarf_planet.csv' dwarfplanet2"
