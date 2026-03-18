#!/bin/sh

#
# Time-stamp: <2025/10/03 13:35:14 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 element.db ".schema --indent"
