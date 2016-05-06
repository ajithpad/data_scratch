import numpy as np
import pylab as pl
import seaborn as sbn
from scipy.stats import norm

fig = pl.figure(1)

xs = [norm.pdf(x,0,10) for x in np.arange(-100,100,0.05)]
pl.plot(np.arange(-100,100,0.05),xs)

xs = [norm.cdf(x,0,10) for x in np.arange(-100,100,0.05)]
pl.plot(np.arange(-100,100,0.05),xs)
pl.show()