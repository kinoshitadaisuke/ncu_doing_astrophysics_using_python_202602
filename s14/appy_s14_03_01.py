#!/usr/pkg/bin/python3

#
# Time-stamp: <2025/12/08 22:55:55 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'star_planet.bin'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# printing simulation object
print (sim)
