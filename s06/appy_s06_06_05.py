#!/usr/bin/env python3

#
# Time-stamp: <2026/03/20 13:49:58 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # getting table information
    table_info = connection.sql ('DESCRIBE landolt')
    # printing table information
    print (table_info)
