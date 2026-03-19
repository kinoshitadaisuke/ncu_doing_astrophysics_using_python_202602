#!/bin/sh

#
# Time-stamp: <2026/03/19 10:35:44 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 element.db ".schema --indent"
