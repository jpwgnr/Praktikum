import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
import scipy.constants as const

plt.rcParams.update({'font.size': 22})

I_vert = 2.28 *0.1
B = const.mu_0 * 8 * 20 * I_vert /(np.sqrt(125)*0.11735)

f, hor1, sweep1, hor2, sweep2 = np.genfromtxt("data/data.txt", unpack=True)

f= f*1000
hor1 = (hor1-13.9)*0.3 
hor2 = (hor2-13.9)*0.3 
sweep1 = sweep1*0.1
sweep2 = sweep2*0.1

sweep1_B = const.mu_0 * 8 * 11 * sweep1/(np.sqrt(125)*0.1639)
sweep2_B = const.mu_0 * 8 * 11 * sweep2/(np.sqrt(125)*0.1639)

hor1_B = const.mu_0 * 8 * 154 * hor1/(np.sqrt(125)*0.1579)
hor2_B = const.mu_0 * 8 * 154 * hor2/(np.sqrt(125)*0.1579)

B1 = sweep1_B + hor1_B 
B2 = sweep2_B + hor2_B

def func(x, m, n):
    return m*x + n 

param1, cov1 = curve_fit(func, f, B1)
err1 = np.sqrt(np.diag(cov1))
a1 = ufloat(param1[0], err1[0])
b1 = ufloat(param1[1], err1[1])

gf1 = const.h/const.value("Bohr magneton") /a1

param2, cov2 = curve_fit(func, f, B2)
err2 = np.sqrt(np.diag(cov2))
a2 = ufloat(param2[0], err2[0])
b2 = ufloat(param2[1], err2[1])

gf2 = const.h/const.value("Bohr magneton") /a2

plt.figure(figsize=(15,8))
plt.plot(f, B1, "x", label="Daten")
plt.plot(f, B2, "x", label="Daten")
plt.plot(f, func(f, *param1), label="Fit")
plt.plot(f, func(f, *param2), label="Fit")
plt.legend(loc="best")
plt.savefig("plots/fits.pdf") 

f=  open("plots/results.txt", "w")
f.write(f"B_Erdmagnetfeld: {B}\n")
f.write(f"Peak 1: a1 = {a1}, b1 = {b1}\n")
f.write(f"Peak 2: a2 = {a2}, b2 = {b2}\n")
f.write(f"gf: {gf1}")

f.close()


