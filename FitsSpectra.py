from astropy.io import fits as pyfits
#import numpy as np

#the data is taken from https://fits.gsfc.nasa.gov/fits_samples.html 
#We're using the FITS called IUE LWP  (spectrum contained in vector columns of a binary table.)
#Each of the sample spectra on this site seem to have different formats.

hdulist = pyfits.open( "IUE.fits" )

# we have 2 HDUs
# The spectral data would seem to be the second HDU
# pretty print its header
print(repr(hdulist[1].header))

# print column information
print(hdulist[1].columns)

spectra = hdulist[1].data

# The column names in spectra are 
# APERTUTE, NPOINTS, WAVELENGTH, DELTAW, 
# NET. BACKGROUND,SIGMA, QUALTIY, FLUX
# The last 5 have 640 values. 

net = spectra[0][5]
flux = spectra[0][8]

# To plot using maptplotlib:
import matplotlib.pyplot as plt
plt.plot(net, flux)
plt.show() # this gives something that looks like a spectra. 
#Presumaby we have to allow fpr BACKGROUND ? 
#Why is the x-axis column called NET?
#Have I even picked the correct columns to plot?
