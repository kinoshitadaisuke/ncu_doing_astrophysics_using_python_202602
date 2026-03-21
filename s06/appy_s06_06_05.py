#!/usr/bin/env python3

#
# Time-stamp: <2026/03/21 16:32:52 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # getting table information
    table_info = connection.sql ('DESCRIBE landolt').fetchall ()
    # printing table information
    for row in table_info:
        for column in row:
            print (f'  {str (column):10s}', end="")
        print ()
