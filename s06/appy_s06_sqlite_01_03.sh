#!/bin/sh

#
# Time-stamp: <2025/10/03 13:35:23 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column element.db \
	"select Symbol, Name, AtomicMass, StandardState, \
	MeltingPoint, BoilingPoint from element \
	where StandardState is 'Liquid';"
