#!/bin/sh

#
# Time-stamp: <2026/03/19 10:37:28 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column ngc2000.db \
	"select id,type,constellation,size,mag from ngc2000 \
	where mag < 4.0 order by mag;"
