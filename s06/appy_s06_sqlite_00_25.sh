#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:18 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 dwarf_planet.db ".schema --indent"
