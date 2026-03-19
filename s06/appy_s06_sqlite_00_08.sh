#!/bin/sh

#
# Time-stamp: <2026/03/19 10:32:58 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Mars', 6.42E23, 6.792E3, 24.6, \
	687.0, -65, 2, 'No', 'No');"
