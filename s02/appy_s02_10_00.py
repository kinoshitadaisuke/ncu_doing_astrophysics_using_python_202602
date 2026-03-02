#!/usr/bin/env python3

#
# Time-stamp: <2026/03/01 11:02:37 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_stars = 'https://s3b.astro.ncu.edu.tw/appy_202602/data/stars.json'

# output data file
file_stars = 'stars.json'

# opening URL
with urllib.request.urlopen (url_stars) as fh_in:
    # reading data
    data_stars = fh_in.read ()

# opening file for writing
with open (file_stars, 'w') as fh_out:
    # writing data into file
    fh_out.write (data_stars.decode ('utf-8'))
