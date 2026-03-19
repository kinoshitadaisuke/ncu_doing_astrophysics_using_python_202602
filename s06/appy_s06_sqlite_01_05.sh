#!/bin/sh

#
# Time-stamp: <2026/03/19 10:36:01 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column element.db \
	"select Name, Symbol, StandardState, MeltingPoint, BoilingPoint \
	from element where BoilingPoint < 300 order by BoilingPoint;"
