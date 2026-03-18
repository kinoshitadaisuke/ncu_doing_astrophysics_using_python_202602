#!/bin/sh

#
# Time-stamp: <2025/10/03 13:36:44 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column bsc5.db \
	"select hr, name, ra_str, dec_str, glon, glat, vmag from bsc \
	where glat > 85.0 order by glat desc;"
