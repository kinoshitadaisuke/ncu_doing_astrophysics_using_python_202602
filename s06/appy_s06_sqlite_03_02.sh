#!/bin/sh

#
# Time-stamp: <2025/10/03 13:37:05 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column hip.db \
	"select hip, ra_hms, dec_dms, vmag, bv, parallax, sptype from hip \
	where hip <= 10 order by hip;"
