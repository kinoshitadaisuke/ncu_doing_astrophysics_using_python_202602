#!/usr/bin/env python3

#
# Time-stamp: <2026/03/03 10:00:24 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_zipfile = 'https://s3b.astro.ncu.edu.tw/appy_202602/data/files2.zip'

# output data file
file_zipfile = 'files2.zip'

# opening URL
with urllib.request.urlopen (url_zipfile) as fh_in:
    # reading data
    data_zipfile = fh_in.read ()

# opening file for writing
with open (file_zipfile, 'wb') as fh_out:
    # writing data into file
    fh_out.write (data_zipfile)
