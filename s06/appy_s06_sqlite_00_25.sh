#!/bin/sh

#
# Time-stamp: <2025/10/03 13:33:48 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 dwarf_planet.db ".schema --indent"
