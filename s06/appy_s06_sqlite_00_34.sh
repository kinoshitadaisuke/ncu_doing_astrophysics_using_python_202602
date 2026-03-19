#!/bin/sh

#
# Time-stamp: <2026/03/19 10:34:59 (UT+08:00) daisuke>
#

# exporting database
sqlite3 dwarf_planet.db ".dump" > dwarf_planet.sql
