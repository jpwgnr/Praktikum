import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
import scipy.constants as const

plt.rcParams.update({'font.size': 24})

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

gj = 2.0023
gf1 = const.h/const.value("Bohr magneton") /a1
I1 = 0.5*(gj/gf1 -1)

param2, cov2 = curve_fit(func, f, B2)
err2 = np.sqrt(np.diag(cov2))
a2 = ufloat(param2[0], err2[0])
b2 = ufloat(param2[1], err2[1])

gf2 = const.h/const.value("Bohr magneton") /a2
I2 = 0.5*(gj/gf2 -1)

plt.figure(figsize=(15,8))
plt.grid()
plt.xlabel(r"$f$ / kHz")
plt.ylabel(r"$B$ / $\mu$T")
plt.plot(f*1e-3, B1*1e6, "x", color="C0", markersize=16, alpha=20, label="Peak 1")
plt.plot(f*1e-3, B2*1e6, "x", color="C1", markersize=16, alpha=20, label="Peak 2")
f_new = np.linspace(min(f)-100e3, max(f)+100e3)
plt.plot(f_new*1e-3, func(f_new, *param1)*1e6, color="C0", linewidth=5,label="Ausgleichsgerade 1")
plt.plot(f_new*1e-3, func(f_new, *param2)*1e6, color="C1", linewidth=5, label="Ausgleichsgerade 2")
plt.legend(loc="best")
plt.savefig("plots/fits.pdf") 

np.savetxt("data/f.txt", f)
np.savetxt("data/hor1.txt", hor1)
np.savetxt("data/hor2.txt", hor2)
np.savetxt("data/sweep1.txt", sweep1)
np.savetxt("data/sweep2.txt", sweep2)
np.savetxt("data/B1.txt", B1)
np.savetxt("data/B2.txt", B2)

f=  open("plots/results.txt", "w")
f.write(f"B_Erdmagnetfeld: {B}\n")
f.write(f"Peak 1: a1 = {a1}, b1 = {b1}\n")
f.write(f"Peak 2: a2 = {a2}, b2 = {b2}\n")
f.write(f"gf: gf1 = {gf1}, gf2 = {gf2}\n")
f.write(f"I: I1 = {I1}, I2 = {I2}\n")



f.close()


