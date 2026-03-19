#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:32 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db "select * from dwarfplanet;"
