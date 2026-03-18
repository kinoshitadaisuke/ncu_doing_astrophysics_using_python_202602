#!/bin/sh

#
# Time-stamp: <2025/10/03 13:32:06 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Mercury', 3.30E23, 4.879E3, 1407.6, \
	88.0, 167, 0, 'No', 'Yes');"
