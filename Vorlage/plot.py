import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 


a = np.linspace(1, 100)
b = np.log(a)


plt.plot(a, b, label="\si{\meter\second}")
plt.legend()
plt.savefig("new.pdf")