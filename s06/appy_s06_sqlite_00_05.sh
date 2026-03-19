#!/bin/sh

#
# Time-stamp: <2026/03/19 10:32:47 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Mercury', 3.30E23, 4.879E3, 1407.6, \
	88.0, 167, 0, 'No', 'Yes');"
