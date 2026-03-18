#!/bin/sh

#
# Time-stamp: <2025/10/03 13:34:08 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db "select * from dwarfplanet;"
