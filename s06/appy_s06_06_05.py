#!/usr/bin/env python3

#
# Time-stamp: <2026/03/21 16:46:40 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # getting table information
    table_info = connection.sql ('DESCRIBE landolt').df ()
    # printing table information
    print (table_info)
