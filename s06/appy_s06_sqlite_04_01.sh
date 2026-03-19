#!/bin/sh

#
# Time-stamp: <2026/03/19 10:37:01 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 mpcorb.db ".schema --indent"
