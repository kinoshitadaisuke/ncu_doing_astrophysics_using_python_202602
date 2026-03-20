#!/usr/bin/env python3

#
# Time-stamp: <2026/03/20 14:00:55 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# SQL command to carry out a query
sql_query = "SELECT name,ra,dec,mag_v,colour_bv,nobs,nnight FROM landolt WHERE nnight > 100 ORDER BY nnight DESC;"

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # executing a query
    query_result = connection.sql (sql_query).show ()
    # printing result of query
    print (query_result)
