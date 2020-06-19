import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

plt.rcParams.update({'font.size': 22})

# Stabilitaetsbedingung

dist, intensity = np.genfromtxt("data/stability1.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"$d /$ cm")
plt.ylabel(r"$P /$ mW")
plt.grid()
plt.plot(dist, intensity, "x", label="Datenpunkte", color="red")
plt.legend()
plt.savefig("plots/stability140.pdf")

dist2, intensity2 = np.genfromtxt("data/stability2.txt", unpack=True)

plt.figure(figsize=(15,8))
plt.xlabel(r"$d /$ \cm")
plt.ylabel(r"$P /$ mW")
plt.grid()
plt.plot(dist2, intensity2, "x", label="Datenpunkte", color="red")
plt.legend()
plt.savefig("plots/stability_flat.pdf")

# Moden Messung

x0, mode0 = np.genfromtxt("data/mode0.txt", unpack=True)

def model0(x, mu, w, I0):
    return I0* (2**0.5/w)**2 * np.exp(-((x - mu)/w)**2)

params0, pcov0 = curve_fit(model0, x0, mode0, p0=[6, 2, 300])
errs0 = np.sqrt(np.diag(pcov0))
ufloats0 = [ufloat(i,j) for i,j in zip(params0,errs0)]
x_new = np.linspace(min(x0), max(x0), 1000)

plt.figure(figsize=(15,8))
plt.xlabel(r"$x$ / cm")
plt.ylabel(r"$I$ / $\mathrm{\mu}$A")
plt.grid()
plt.plot(x_new, model0(x_new, *params0), label="Ausgleichskurve")
plt.plot(x0, mode0, "x", label="Datenpunkte")
plt.legend()
plt.savefig("plots/mode0.pdf")





x1, mode1 = np.genfromtxt("data/mode1.txt", unpack=True)

def model1(x, mu, w, I0):
    return I0* (2**0.5 *2 *(x - mu)/w)**2 * (2**0.5/w)**2 *np.exp(-((x - mu)/w)**2)

params1, pcov1 = curve_fit(model1, x1, mode1, p0=[6, 4, 10])
errs1 = np.sqrt(np.diag(pcov1))
ufloats1 = [ufloat(i,j) for i,j in zip(params1,errs1)]
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




x2, mode2 = np.genfromtxt("data/mode2.txt", unpack=True)

def model2(x, mu, w, I0):
    return I0* ( 4*(2**0.5 * (x - mu)/w)**2 -2)**2 *(2**0.5/w)**2 *np.exp(-((x - mu)/w)**2)

params2, pcov2 = curve_fit(model2, x2, mode2, p0=[6, 3, 1])
errs2 = np.sqrt(np.diag(pcov2))
ufloats2 = [ufloat(i,j) for i,j in zip(params2,errs2)]
x2_new = np.linspace(min(x2), max(x2), 1000)

plt.figure(figsize=(15,8))
plt.xlabel(r"$x$ / cm")
plt.ylabel(r"$I$ / $\mathrm{\mu}$A")
plt.grid()
plt.plot(x2_new, model2(x2_new,*params2), label="Ausgleichskurve")
plt.plot(x2, mode2, "x", label="Datenpunkte")
plt.legend()
plt.savefig("plots/mode2.pdf")

# polarisation

phi, polar = np.genfromtxt("data/polarisation.txt", unpack=True)

def pol(phi, amp, delta):
    return amp* np.cos(np.deg2rad(phi+delta))**2

params_pol, pcov_phi = curve_fit(pol, phi, polar, p0=[2, 100])
errs_pol = np.sqrt(np.diag(pcov_phi))
ufloats_pol = [ufloat(i,j) for i,j in zip(params_pol,errs_pol)]
phi_new = np.linspace(min(phi)-10, max(phi)+10, 1000)

plt.figure(figsize=(15,8))
plt.xlabel(r"$\phi$ / °")
plt.ylabel(r"$P$ / mW")
plt.grid()
plt.plot(phi_new, pol(phi_new,*params_pol), label="Ausgleichskurve")
plt.plot(phi, polar, "x", label="Datenpunkte")
plt.legend()
plt.savefig("plots/polarisation.pdf")



# Wellenlaenge

# def lambda_(d, gitter, a):
#     return d * a


lambda100 = 0.001/100*0.021/np.sqrt(0.021**2 + 0.325**2) #(np.sin(np.tan(0.021/0.325))* 0.001/100)
lambda600 = 0.001/600*0.053/np.sqrt(0.053**2 + 0.125**2)
lambda80 = 0.001/80*0.012/np.sqrt(0.012**2 + 0.225**2)


f=  open("plots/results.txt", "w")
f.write(f" \t\tTEM_00 \t\t\t\tTEM_10  \t\t\tTEM_20 \n")
f.write(f"mu: \t{ufloats0[0]} cm,\t{ufloats1[0]} cm,\t{ufloats2[0]} cm\n")
f.write(f"w: \t\t{ufloats0[1]} cm,\t{ufloats1[1]} cm,\t{ufloats2[1]} cm\n")
f.write(f"I_0: \t{ufloats0[2]} muA,\t\t{ufloats1[2]} muA,\t{ufloats2[2]} muA\n\n")
f.write(f"Amplitude: \t{ufloats_pol[0]} mW,\t delta: {ufloats_pol[1]} \n\n")
f.write(f"Lambda (100/mm): {lambda100:.4e}\n")
f.write(f"Lambda (600/mm): {lambda600:.4e}\n")
f.write(f"Lambda (80/mm): {lambda80:.4e}\n")
f.close()