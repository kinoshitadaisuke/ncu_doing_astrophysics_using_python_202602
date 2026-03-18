#!/bin/sh

#
# Time-stamp: <2025/10/03 13:37:30 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column mpcorb.db \
	"select designation,name,a,e,i,absmag from mpcorb \
	where absmag < 3 and absmag > -100 order by absmag;"
