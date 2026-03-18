#!/bin/sh

#
# Time-stamp: <2025/10/03 13:34:34 (UT+08:00) daisuke>
#

# exporting database
sqlite3 dwarf_planet.db ".dump" > dwarf_planet.sql
