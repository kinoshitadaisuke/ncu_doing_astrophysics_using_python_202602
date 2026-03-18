#!/bin/sh

#
# Time-stamp: <2025/10/03 13:32:16 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Earth', 5.97E24, 1.2756E4, 23.9, \
	365.2, 15, 1, 'No', 'Yes');"
