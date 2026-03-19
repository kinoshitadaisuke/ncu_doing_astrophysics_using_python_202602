#!/bin/sh

#
# Time-stamp: <2026/03/19 10:33:09 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Uranus', 8.68E25, 5.1118E4, -17.2, \
	30589, -195, 27, 'Yes', 'Yes');"
