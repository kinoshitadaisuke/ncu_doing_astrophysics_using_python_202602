#!/usr/bin/env python3

#
# Time-stamp: <2026/03/21 16:43:28 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# database file
file_db = 'landolt_2009.db'

# SQL command to carry out a query
sql_query = "SELECT name,mag_v,colour_ub,colour_bv,colour_vr,colour_ri FROM landolt WHERE colour_ub > 1.2 and colour_bv > 1.2 and colour_vr > 1.2 and colour_ri > 1.2 ORDER BY mag_v;"

# connecting to a new database
with duckdb.connect (file_db) as connection:
    # executing a query
    query_result = connection.sql (sql_query).df ()
    # printing result of query
    print (query_result)
