#!/bin/sh

#
# Time-stamp: <2026/03/19 10:32:43 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 planet0.db ".schema --indent"
