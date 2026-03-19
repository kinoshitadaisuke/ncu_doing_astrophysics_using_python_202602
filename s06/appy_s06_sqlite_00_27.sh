#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:25 (UT+08:00) daisuke>
#

# importing data from CSV file
sqlite3 dwarf_planet.db ".import --csv --skip 16 dwarf_planet.csv dwarfplanet"
