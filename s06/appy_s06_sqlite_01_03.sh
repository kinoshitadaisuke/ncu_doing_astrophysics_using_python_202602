#!/bin/sh

#
# Time-stamp: <2026/03/19 10:35:52 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column element.db \
	"select Symbol, Name, AtomicMass, StandardState, \
	MeltingPoint, BoilingPoint from element \
	where StandardState is 'Liquid';"
