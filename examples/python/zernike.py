#!/usr/bin/env python
"""
LightPipes for Python Optical Toolbox

Example from the old C-based command line manual:
Figure 14: The intensity in the input plane and after propagation through a
cylindrical system, defined as a combination of Zernike polynomials and free
space propagation. 

The result of propagation to the focal plane of cylindric lens, defined as a
combination of two Zernike polynomials, is shown in Fig. 14.
"""

import common
from lightpipes import Field
from pylab import *

m=1
nm=1e-9*m
mm=1e-3*m
cm=1e-2*m

ion()

F = Field( 256, 0.01, 1e-6 )    \
  .gaussian_aperture( 0.00225 ) \
  .zernike( 2, 2, 0.0045, 20)   \
  .zernike( 2, 0, 0.0045, -10)  \
  .fresnel(1.55)                \
  .interpolate( angle=pi/32 ) # example of rotating the grid

imshow( (F.value * F.value.conj()).real )
title('Intensity')
draw()
print 'press enter to show phase'
raw_input()

imshow( angle(F.value) )
title('Phase')
draw()
print 'press enter to exit'
raw_input()
