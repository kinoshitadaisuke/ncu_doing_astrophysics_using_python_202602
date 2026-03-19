#!/bin/sh

#
# Time-stamp: <2026/03/19 10:32:51 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Venus', 4.87E24, 1.2104E4, -5832.5, \
	224.7, 464, 0, 'No', 'No');"
