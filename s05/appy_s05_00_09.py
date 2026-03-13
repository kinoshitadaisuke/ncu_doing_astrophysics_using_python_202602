#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/30 20:50:08 (UT+08:00) daisuke>
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
