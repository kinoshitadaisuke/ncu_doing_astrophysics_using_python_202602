#!/bin/sh

#
# Time-stamp: <2025/10/03 13:34:48 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet3.db \
	"select * from dwarfplanet where i > 20 order by i desc;"
