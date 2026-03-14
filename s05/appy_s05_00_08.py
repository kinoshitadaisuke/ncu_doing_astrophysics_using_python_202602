#!/usr/bin/env python3

#
# Time-stamp: <2026/03/14 21:15:02 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# nano
nano = scipy.constants.nano

# wavelength of electromagnetic radiation
wavelength = 500.0 * nano

# frequency of electromagnetic radiation
frequency = scipy.constants.lambda2nu (wavelength)

# printing the result of conversion
print (f'{wavelength:g} [m] ==> {frequency:g} [Hz]')
