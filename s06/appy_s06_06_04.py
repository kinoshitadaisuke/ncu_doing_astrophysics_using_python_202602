#!/usr/bin/env python3

#
# Time-stamp: <2026/03/21 16:27:36 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # getting a list of tables
    list_tables = connection.sql ('SHOW TABLES').fetchall ()
    # printing a list of tables
    for table in list_tables:
        print (table)
