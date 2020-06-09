import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

# Stabilitätsbedingung

dist, intensity = np.genfromtxt("data/stability1.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"$d /$ cm")
plt.ylabel(r"$P /$ mW")
plt.grid()
plt.plot(dist, intensity, "x", label="data", color="red")
plt.legend()
plt.savefig("plots/stability140.pdf")

dist2, intensity2 = np.genfromtxt("data/stability2.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"$d /$ \cm")
plt.ylabel(r"$P /$ mW")
plt.grid()
plt.plot(dist2, intensity2, "x", label="data", color="red")
plt.legend()
plt.savefig("plots/stability_flat.pdf")

# Moden Messung

x0, mode0 = np.genfromtxt("data/mode0.txt", unpack=True)

def model0(x, mu, sigma, a):
    return a*np.exp(-0.5*((x - mu)/sigma)**2)

params0, pcov0 = curve_fit(model0, x0, mode0, p0=[6, 2, 300])
x_new = np.linspace(min(x0), max(x0), 1000)
plt.figure(figsize=(15,8))
plt.xlabel(r"$x$ / cm")
plt.ylabel(r"$I$ / $\mathrm{\mu}$A")
plt.grid()
plt.plot(x_new, model0(x_new, *params0), label="Ausgleichskurve")
plt.plot(x0, mode0, "x", label="Datenpunkte")
plt.savefig("plots/mode0.pdf")

errs0 = np.sqrt(np.diag(pcov0))

print(params0, errs0)


x1, mode1 = np.genfromtxt("data/mode1.txt", unpack=True)

def model1(x, mu, sigma, a):
    return a* ((x - mu)/sigma)**2 *np.exp(-0.5*((x - mu)/sigma)**2)

params1, pcov1 = curve_fit(model1, x1, mode1, p0=[6, 4, 10])
x1_new = np.linspace(min(x1)-1, max(x1)+1, 1000)

plt.figure(figsize=(15,8))
plt.xlabel(r"$x$ / cm")
plt.ylabel(r"$I$ / $\mathrm{\mu}$A")
plt.grid()
plt.plot(x1_new, model1(x1_new, *params1), label="Ausgleichskurve")
#plt.plot(x1_new, model1(x1_new, 6, 3, -3, 2), label="Ausgleichskurve")
plt.plot(x1, mode1, "x", label="Datenpunkte")
plt.legend()
plt.savefig("plots/mode1.pdf")

errs1 = np.sqrt(np.diag(pcov1))
print(params1, errs1)


x2, mode2 = np.genfromtxt("data/mode2.txt", unpack=True)

def model2(x, mu, sigma, a, b):
    return a* 8*((x - mu)**2/sigma)**2 *np.exp(-0.5*((x - mu)/sigma)**2)

params2, pcov2 = curve_fit(model2, x2, mode2)#, p0=[6, 2, 10, 0])
x2_new = np.linspace(min(x2), max(x2), 1000)

plt.figure(figsize=(15,8))
plt.xlabel(r"$x /$ cm")
plt.ylabel(r"$I /$ \muA")
plt.grid()
plt.plot(x2_new, model2(x2_new,*params2), label="Ausgleichskurve")
plt.plot(x2, mode2, "x", label="Datenpunkte")
plt.savefig("plots/mode2.pdf")

errs2 = np.sqrt(np.diag(pcov2))
print(params2, errs2)
# polarisation

phi, polar = np.genfromtxt("data/polarisation.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"$\phi /$ °")
plt.ylabel(r"$P/$ mW")
plt.grid()
plt.plot(phi, polar, "x", label="Datenpunkte")
plt.savefig("plots/polarisation.pdf")


# Wellenlänge

# def lambda_(d, gitter, a):
#     return d * a


lambda100 = 0.001/100*0.021/np.sqrt(0.021**2 + 0.325**2)
lambda600 = 0.001/600*0.053/np.sqrt(0.053**2 + 0.125**2)
lambda80 = 0.001/80*0.012/np.sqrt(0.012**2 + 0.225**2)