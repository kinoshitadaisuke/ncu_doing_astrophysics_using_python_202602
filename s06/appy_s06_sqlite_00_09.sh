#!/bin/sh

#
# Time-stamp: <2026/03/19 10:33:02 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Jupiter', 1.898E27, 1.42984E5, 9.9, \
	4331, -110, 79, 'Yes', 'Yes');"
