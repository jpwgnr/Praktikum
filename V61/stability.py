import matplotlib.pyplot as plt
import numpy as np
#import uncertainties.unumpy as unp
#from uncertainties import ufloat
#from scipy.optimize import curve_fit

d = np.arange(0., 280., 1.0)
stability1 = (1 - d/140)**2

plt.figure(figsize=(15,8))
plt.xlabel(r"$d /$ cm")
plt.ylabel(r"$g_1 g_2$")
plt.grid()
plt.plot(d, stability1)
plt.axis([0, 280, 0, 1])
plt.savefig("plots/stability1.pdf")

stability2 = (1 - d/140)
plt.figure(figsize=(15,8))
plt.xlabel(r"$d /$ cm")
plt.ylabel(r"$g_1 g_2$")
plt.grid()
plt.plot(d, stability2)
plt.axis([0, 280, 0, 1])
plt.savefig("plots/stability2.pdf")