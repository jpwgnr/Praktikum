import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

lambda_, deg1_1, min1_1, deg1_2, min1_2,  deg2_1, min2_1, deg2_2, min2_2, deg3_1, min3_1, deg3_2, min3_2 = np.genfromtxt("data/data.txt", unpack=True)


# min to deg 
deg1_1 = deg1_1 + min1_1/60 
deg1_2 = deg1_2 + min1_2/60
deg2_1 = deg2_1 + min2_1/60
deg2_2 = deg2_2 + min2_2/60
deg3_1 = deg3_1 + min3_1/60
deg3_2 = deg3_2 + min3_2/60

winkel1 = 0.5*(deg1_1 + deg1_2)
winkel2 = 0.5*(deg2_1 + deg2_2) 
winkel3 = 0.5*(deg3_1 + deg3_2) 

winkel1 = np.deg2rad(winkel1)/5.11e-3
winkel2 = np.deg2rad(winkel2)/1.296e-3
winkel3 = np.deg2rad(winkel3)/1.36e-3

diff2 = winkel2-winkel1 
diff3 = winkel3-winkel1

N2 = 2.8e18
N3 = 1.2e18
n = 1
B = 392e-3

a = const.elementary_charge**3 / (8* np.pi**2 *const.epsilon_0 * const.speed_of_light**3)


def mass(lambda_, m):
    return a * 1/m**2 * lambda_**2 

plt.figure()
plt.plot(lambda_**2, diff2, "x", label="Daten")
plt.legend(loc="best")
plt.savefig("plots/Probe1.pdf")

plt.figure()
plt.plot(lambda_**2, diff3, "x", label="Daten")
plt.legend(loc="best")
plt.savefig("plots/Probe2.pdf")

