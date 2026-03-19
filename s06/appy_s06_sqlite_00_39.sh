#!/bin/sh

#
# Time-stamp: <2026/03/19 10:35:28 (UT+08:00) daisuke>
#

# exporting database into a CSV file
sqlite3 dwarf_planet3.db \
	".header on" \
	".mode csv" \
	".once new.csv" \
	"select * from dwarfplanet;"
