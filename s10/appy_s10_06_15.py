#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/11/03 14:15:59 (UT+08:00) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-2015-2019.git'

# directory name of downloaded repository
dir_repo = 'osc_2015_2019'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
