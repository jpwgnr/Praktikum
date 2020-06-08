import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
#Generate data 


# Stabilitätsbedingung

dist, intensity = np.genfromtxt("stability.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"d / \si{\centi\meter}")
plt.ylabel(r"I / \si{\milli\watt}")
plt.grid()
plt.plot(dist, intensity, "x", label="data", color="red")
plt.legend()
plt.savefig("Plots/stability140.pdf")

dist2, intensity2 = np.genfromtxt("stability2.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"d / \si{\centi\meter}")
plt.ylabel(r"I / \si{\milli\watt}")
plt.grid()
plt.plot(dist2, intensity2, "x", label="data", color="red")
plt.legend()
plt.savefig("Plots/stability_flat.pdf")

# Moden Messung

x0, mode0 = np.genfromtxt("moden.txt", unpack=True)

def model0(x, mu, sigma):
    return np.exp(-(x - mu)/sigma)**2+ b

params, pcov = curve_fit(model0, x0, mode0)

plt.figure(figsize=(15,8))
plt.xlabel(r"x / \si{\centi\meter}")
plt.ylabel(r"I / \si{\micro\ampere}")
plt.grid()
plt.plot(x0, model0(*params), label="Ausgleichskurve")
plt.plot(x0, mode0, label="Datenpunkte")

errs = np.sqrt(np.diag(pcov))

for i in zip(params, errs):
    print(ufloat(i))



x1, mode1 = np.genfromtxt("moden1.txt", unpack=True)

def model1(x, mu, sigma):
    return x* np.exp(-(x - mu)/sigma)**2+ b

params, pcov = curve_fit(model1, x1, mode1)

plt.figure(figsize=(15,8))
plt.xlabel(r"x / \si{\centi\meter}")
plt.ylabel(r"I / \si{\micro\ampere}")
plt.grid()
plt.plot(x1, model1(*params), label="Ausgleichskurve")
plt.plot(x1, mode1, label="Datenpunkte")

errs = np.sqrt(np.diag(pcov))

for i in zip(params, errs):
    print(ufloat(i))



x2, mode2 = np.genfromtxt("moden2.txt", unpack=True)

def model2(x, mu, sigma):
    return x* np.exp(-(x - mu)/sigma)**2+ b

params, pcov = curve_fit(model2, x2, mode2)

plt.figure(figsize=(15,8))
plt.xlabel(r"x / \si{\centi\meter}")
plt.ylabel(r"I / \si{\micro\ampere}")
plt.grid()
plt.plot(x2, model2(*params), label="Ausgleichskurve")
plt.plot(x2, mode2, label="Datenpunkte")

errs = np.sqrt(np.diag(pcov))

for i in zip(params, errs):
    print(ufloat(i))

# polarisation

phi, polar = np.genfromtxt("polar.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"x / \si{\centi\meter}")
plt.ylabel(r"I / \si{\micro\ampere}")
plt.grid()
plt.plot(phi, polar, label="Datenpunkte")


# Wellenlänge

# def lambda_(d, gitter, a):
#     return d * a
