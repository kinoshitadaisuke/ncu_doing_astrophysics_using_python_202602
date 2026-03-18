#!/bin/sh

#
# Time-stamp: <2025/10/03 13:33:44 (UT+08:00) daisuke>
#

# SQL query
sqlite3 dwarf_planet.db \
	"create table dwarfplanet (name text primary key, \
	a real, e real, i real, perihelion real, aphelion real, P real, H real);"
