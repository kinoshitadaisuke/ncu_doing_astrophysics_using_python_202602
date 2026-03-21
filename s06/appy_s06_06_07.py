#!/usr/bin/env python3

#
# Time-stamp: <2026/03/21 16:42:18 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# SQL command to carry out a query
sql_query = "SELECT name,ra,dec,mag_v,colour_bv FROM landolt WHERE mag_v < 9.0 ORDER BY mag_v;"

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # executing a query
    query_result = connection.sql (sql_query).df ()
    # printing result of query
    print (query_result)
