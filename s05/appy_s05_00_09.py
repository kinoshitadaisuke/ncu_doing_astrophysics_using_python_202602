#!/usr/bin/env python3

#
# Time-stamp: <2026/03/14 21:15:12 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# giga
giga = scipy.constants.giga

# frequency of electromagnetic radiation
frequency = 115.0 * giga

# wavelength of electromagnetic radiation
wavelength = scipy.constants.nu2lambda (frequency)

# printing the result of conversion
print (f'{frequency:g} [Hz] ==> {wavelength:g} [m]')
