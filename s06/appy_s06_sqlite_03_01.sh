#!/bin/sh

#
# Time-stamp: <2026/03/19 10:36:40 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 hip.db ".schema --indent"
