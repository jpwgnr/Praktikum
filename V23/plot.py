import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
#from something import some 

plt.rcParams.update({'font.size': 28})

#Generate data

#A) Vorbereitung
#1 bis 12 Zylinder (l=50mm)
f_a2_1, amp_a2_1 = np.genfromtxt("data/a_2_1.dat", unpack=True)
f_a2_2, amp_a2_2 = np.genfromtxt("data/a_2_2.dat", unpack=True)
f_a2_3, amp_a2_3 = np.genfromtxt("data/a_2_3.dat", unpack=True)
f_a2_4, amp_a2_4 = np.genfromtxt("data/a_2_4.dat", unpack=True)
f_a2_5, amp_a2_5 = np.genfromtxt("data/a_2_5.dat", unpack=True)
f_a2_6, amp_a2_6 = np.genfromtxt("data/a_2_6.dat", unpack=True)
f_a2_7, amp_a2_7 = np.genfromtxt("data/a_2_7.dat", unpack=True)
f_a2_8, amp_a2_8 = np.genfromtxt("data/a_2_8.dat", unpack=True)
f_a2_9, amp_a2_9 = np.genfromtxt("data/a_2_9.dat", unpack=True)
f_a2_10, amp_a2_10 = np.genfromtxt("data/a_2_10.dat", unpack=True)
f_a2_11, amp_a2_11 = np.genfromtxt("data/a_2_11.dat", unpack=True)
f_a2_12, amp_a2_12 = np.genfromtxt("data/a_2_12.dat", unpack=True)


f1, f2, laenge = np.genfromtxt("data2/a1.txt", unpack=True)
delta_f = f2-f1
np.savetxt("plots/a1.txt", delta_f)
invers_laenge = 1/(2*laenge)
#1 Zylinder (l=75mm)
f_a3, amp_a3 = np.genfromtxt("data/a_3.dat", unpack=True)


#B) 1-dim Festkörper
#2 bis 10 Zylinder (l=50mm), 1 bis 9 Blenden (d=16mm)
f_b1_2, amp_b1_2 = np.genfromtxt("data/b_1_2.dat", unpack=True)
f_b1_3, amp_b1_3 = np.genfromtxt("data/b_1_3.dat", unpack=True)
f_b1_4, amp_b1_4 = np.genfromtxt("data/b_1_4.dat", unpack=True)
f_b1_5, amp_b1_5 = np.genfromtxt("data/b_1_5.dat", unpack=True)
f_b1_6, amp_b1_6 = np.genfromtxt("data/b_1_6.dat", unpack=True)
f_b1_7, amp_b1_7 = np.genfromtxt("data/b_1_7.dat", unpack=True)
f_b1_8, amp_b1_8 = np.genfromtxt("data/b_1_8.dat", unpack=True)
f_b1_9, amp_b1_9 = np.genfromtxt("data/b_1_9.dat", unpack=True)
f_b1_10, amp_b1_10 = np.genfromtxt("data/b_1_10.dat", unpack=True)

#2,4,10 Zylinder (l=50mm), 1,3,9 Blenden (d=10mm)
f_b2_2, amp_b2_2 = np.genfromtxt("data/b_2_2.dat", unpack=True)
f_b2_4, amp_b2_4 = np.genfromtxt("data/b_2_4.dat", unpack=True)
f_b2_10, amp_b2_10 = np.genfromtxt("data/b_2_10.dat", unpack=True)

#2,4,10 Zylinder (l=50mm), 1,3,9 Blenden (d=13mm)
f_b3_2, amp_b3_2 = np.genfromtxt("data/b_3_2.dat", unpack=True)
f_b3_4, amp_b3_4 = np.genfromtxt("data/b_3_4.dat", unpack=True)
f_b3_10, amp_b3_10 = np.genfromtxt("data/b_3_10.dat", unpack=True)

#10 Zylinder: 9x l=50mm, 1x l=75mm(1)/l=37,5mm(2)/l=62,5mm(3)
f_b4_1, amp_b4_1 = np.genfromtxt("data/b_4_1.dat", unpack=True)
f_b4_2, amp_b4_2 = np.genfromtxt("data/b_4_2.dat", unpack=True)
f_b4_3, amp_b4_3 = np.genfromtxt("data/b_4_3.dat", unpack=True)

#10 Zylinder (abwechselnd l=50mm und l=75mm), 9 Blenden (d=16mm)
f_b5, amp_b5 = np.genfromtxt("data/b_5.dat", unpack=True)

#8 Zylinder (l=50mm), 7 Blenden (abwechselnd d=13mm und d=16mm)
f_b6, amp_b6 = np.genfromtxt("data/b_6.dat", unpack=True)


#C) H-Atom
#180°
f_c1, amp_c1 = np.genfromtxt("data/c_1.dat", unpack=True)


#selbst abgelesen bei 2,3kHz: Winkel und Maximum Amplitude
phi_1, amp_1 = np.genfromtxt("data2/polar_atom1.txt", unpack=True)

#selbst abgelesen bei 3,7kHz: Winkel und Maximum Amplitude
phi_2, amp_2 = np.genfromtxt("data2/polar_atom2.txt", unpack=True)

#selbst abgelesen bei 7,4kHz: Winkel und Maximum Amplitude
phi_3, amp_3 = np.genfromtxt("data2/polar_atom3.txt", unpack=True)

#selbst abgelesen bei xy kHz: Winkel und Maximum Amplitude
phi_4, amp_4 = np.genfromtxt("data2/polar_atom4.txt", unpack=True)

#180° mit Zwischenring (Dicke h=3mm/h=6mm/h=9mm)
f_c4_1, amp_c4_1 = np.genfromtxt("data/c_4_1.dat", unpack=True)
f_c4_2, amp_c4_2 = np.genfromtxt("data/c_4_2.dat", unpack=True)
f_c4_3, amp_c4_3 = np.genfromtxt("data/c_4_3.dat", unpack=True)

#Aufspaltung gegen Ringdicke
dicke, aufspaltung = np.genfromtxt("data2/aufspaltung.txt", unpack=True)

#selbst abgelesen bei 2,3kHz & Zw.ring: Winkel und Maximum Amplitude
phi_5, amp_5, amp_5_1 = np.genfromtxt("data2/polar_atom5.txt", unpack=True)


#D) H-Molekuel
#Zwei Kugeln, 180°, ohne Blende
f_d1_1, amp_d1_1 = np.genfromtxt("data/d_1_1.dat", unpack=True)

#Zwei Kugeln, 180°, mit Blende (d=10mm/d=13mm/d=16mm)
f_d1_2, amp_d1_2 = np.genfromtxt("data/d_1_2.dat", unpack=True)
f_d1_3, amp_d1_3 = np.genfromtxt("data/d_1_3.dat", unpack=True)
f_d1_4, amp_d1_4 = np.genfromtxt("data/d_1_4.dat", unpack=True)

#Resonanzfreq. gegen Blendendurchmesser
durchmesser, frequenz1, frequenz2, frequenz3 = np.genfromtxt("data2/resonanzen.txt", unpack=True)

#selbst abgelesen bei 2,3kHz & Blende: Winkel und Maximum Amplitude
phi_6, amp_6 = np.genfromtxt("data2/polar_molekuel.txt", unpack=True)

def func(x, c):
    return x*c

params, cov = curve_fit(func, invers_laenge, delta_f)
err = np.sqrt(np.diag(cov))
c = ufloat(params[0], err[0])
print(c)
# Plots erstellen

new_laenge = np.linspace(min(invers_laenge)-0.5, max(invers_laenge)+0.5)

fig_1 = plt.figure(figsize=(15,8))
plt.ylabel(r"$f$ / kHz")
plt.xlabel(r"1/$(2L)$ / 1/m")
plt.plot(invers_laenge, delta_f*1e-3, "x", mew=3, markersize=16, label="Messwerte")
plt.plot(new_laenge, func(new_laenge, *params)*1e-3, linewidth=4, label="Ausgleichsgerade")
plt.grid()
plt.legend(loc="best")
plt.savefig("plots/A_2.pdf")


#1 Zylinder (l=75mm)
fig_2 = plt.figure(figsize=(15,8))
ax1 = fig_2.add_subplot(111)
ax1.set_xlabel(r"$f$ / kHz")
ax1.set_ylabel(r"Amplitude / (a.u.)")
plt.grid()
ax1.plot(f_a3[178:]*1e-3, amp_a3[178:], linewidth=4, label="Messwerte")
plt.legend()
plt.savefig("plots/A_3.pdf")


#B
#2 bis 10 Zylinder (l=50mm), 1 bis 9 Blenden (d=16mm)
fig_3 = plt.figure(figsize=(15,20))
ax1 = fig_3.add_subplot(3,1,1)
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b1_2[178:]*1e-3, amp_b1_2[178:], linewidth=4, label="2 Segmente")
ax1.grid()
ax1.legend()
ax4 = fig_3.add_subplot(3,1,2)
ax4.set_ylabel(r"Amplitude/ (a.u.)")
ax4.plot(f_b1_5[178:]*1e-3, amp_b1_5[178:], linewidth=4, label="4 Segmente")
ax4.grid()
ax4.legend()
ax9 = fig_3.add_subplot(3,1,3)
ax9.set_xlabel(r"$f$/kHz")
ax9.set_ylabel(r"Amplitude/ (a.u.)")
ax9.plot(f_b1_10[178:]*1e-3, amp_b1_10[178:], linewidth=4, label="10 Segmente")
ax9.grid()
ax9.legend()
plt.savefig("plots/B_1.pdf")

#2,4,10 Zylinder (l=50mm), 1,3,9 Blenden (d=10mm)
fig_4 = plt.figure(figsize=(24,20))
ax1 = fig_4.add_subplot(321)
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_b2_2[178:]*1e-3, amp_b2_2[178:], linewidth=4, label="2 Segmente, 10 mm")
ax1.grid()
ax1.legend()
ax2 = fig_4.add_subplot(323)
ax2.set_ylabel(r"Amplitude / (a.u.)")
ax2.plot(f_b2_4[178:]*1e-3, amp_b2_4[178:], linewidth=4, label="4 Segmente, 10 mm")
ax2.grid()
ax2.legend()
ax3 = fig_4.add_subplot(325)
ax3.set_xlabel(r"$f$ / kHz")
ax3.set_ylabel(r"Amplitude / (a.u.)")
ax3.plot(f_b2_10[178:]*1e-3, amp_b2_10[178:], linewidth=4, label="10 Segmente, 10 mm")
ax3.grid()
ax3.legend()
#2,4,10 Zylinder (l=50mm), 1,3,9 Blenden (d=13mm)
ax4 = fig_4.add_subplot(322)
ax4.set_ylabel(r"Amplitude/ (a.u.)")
ax4.plot(f_b3_2[178:]*1e-3, amp_b3_2[178:], linewidth=4, label="2 Segmente, 13 mm")
ax4.grid()
ax4.legend()
ax5 = fig_4.add_subplot(324)
ax5.set_ylabel(r"Amplitude/ (a.u.)")
ax5.plot(f_b3_4[178:]*1e-3, amp_b3_4[178:], linewidth=4, label="4 Segmente, 13 mm")
ax5.grid()
ax5.legend()
ax6 = fig_4.add_subplot(326)
ax6.set_xlabel(r"$f$ / kHz")
ax6.set_ylabel(r"Amplitude/ (a.u.)")
ax6.plot(f_b3_10[178:]*1e-3, amp_b3_10[178:], linewidth=4, label="10 Segmente, 13 mm")
ax6.grid()
ax6.legend()
plt.savefig("plots/B_3.pdf")

#10 Zylinder: 9x l=50mm, 1x l=75mm(1)/l=37,5mm(2)/l=62,5mm(3)
fig_6 = plt.figure(figsize=(24,20))
ax1 = fig_6.add_subplot(321)
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_b4_1[178:]*1e-3, amp_b4_1[178:], linewidth=4, label="9 Segmente 50 mm,\n1 Segment 75 mm")
ax1.grid()
ax1.legend()
ax2 = fig_6.add_subplot(325)
ax2.set_xlabel(r"$f$ / kHz")
ax2.set_ylabel(r"Amplitude / (a.u.)")
ax2.plot(f_b4_2[178:]*1e-3, amp_b4_2[178:], linewidth=4, label="9 Segmente 50 mm,\n1 Segment 37,5 mm")
ax2.grid()
ax2.legend()
ax3 = fig_6.add_subplot(323)
ax3.set_ylabel(r"Amplitude / (a.u.)")
ax3.plot(f_b4_3[178:]*1e-3, amp_b4_3[178:], linewidth=4, label="9 Segmente 50 mm,\n1 Segment 62,5 mm")
ax3.grid()
ax3.legend()

#10 Zylinder (abwechselnd l=50mm und l=75mm), 9 Blenden (d=16mm) & Vgl ein Zylinder l=50mm und ein Zylinder l=75mm
ax4 = fig_6.add_subplot(322)
ax4.set_ylabel(r"Amplitude / (a.u.)")
ax4.plot(f_b5[178:]*1e-3, amp_b5[178:], linewidth=4, label="10 Segmente \nwechselnd 50/75 mm")
ax4.grid()
ax4.legend()
ax5 = fig_6.add_subplot(324)
ax5.set_ylabel(r"Amplitude / (a.u.)")
ax5.plot(f_a2_1[178:]*1e-3, amp_a2_1[178:], linewidth=4, label="1 Segment 50 mm")
ax5.grid()
ax5.legend()
ax6 = fig_6.add_subplot(326)
ax6.set_xlabel(r"$f$ / kHz")
ax6.set_ylabel(r"Amplitude / (a.u.)")
ax6.plot(f_a3[178:]*1e-3, amp_a3[178:], linewidth=4, label="1 Segment 75 mm")
ax6.grid()
ax6.legend()
plt.savefig("plots/B_5.pdf")

#8 Zylinder (l=50mm), 7 Blenden (abwechselnd d=13mm und d=16mm)
fig_8 = plt.figure(figsize=(15,8))
ax1 = fig_8.add_subplot(111)
ax1.set_xlabel(r"$f$ / kHz")
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_b6[178:]*1e-3, amp_b6[178:], linewidth=4, label="8 Segmente 50 mm, \nBlenden wechselnd 13/16 mm")
ax1.grid()
ax1.legend()
plt.savefig("plots/B_6.pdf")


#C
#180°
fig_9 = plt.figure(figsize=(15,8))
ax1 = fig_9.add_subplot(111)
ax1.set_xlabel(r"$f$ / kHz")
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_c1*1e-3, amp_c1, linewidth=4, label=r"Kugelresonator, $\alpha$=180°")
ax1.grid()
ax1.legend()
plt.savefig("plots/C_1.pdf")

def legend0(phi, a):
    return np.abs(a* np.cos(phi)**0)

def legend1(phi, a):
    return np.abs(a* np.cos(phi))

def legend2(phi, a):
    return np.abs(a* 0.5*(3*np.cos(phi)**2 -1))

def legend3(phi, a):
    return np.abs(a* 0.5*(5*np.cos(phi)**3 -3*np.cos(phi)))

phi = np.linspace(0, 2*np.pi, 1000)

param0, cov0 = curve_fit(legend0, np.deg2rad(phi_1[8:]), amp_1[8:])
err0 = np.sqrt(np.diag(cov0))
a0 = ufloat(param0[0], err0[0])
print(a0)
#Polarplot 2,3kHz
fig_10 = plt.figure(figsize=(25,25))
ax1 =fig_10.add_subplot(221, projection='polar')
ax1.plot(np.deg2rad(phi_1), amp_1, 'x', mew=3, markersize=16, label="Messwerte")
ax1.plot(phi, legend0(phi, *param0),linewidth=4, label="Ausgleichskurve")
ax1.legend()

param1, cov1 = curve_fit(legend1, np.deg2rad(phi_2[8:]), amp_2[8:])
err1 = np.sqrt(np.diag(cov1))
a1 = ufloat(param1[0], err1[0])
print(a1)
#Polarplot 3,7kHz
ax2 =fig_10.add_subplot(222, projection='polar')
ax2.plot(np.deg2rad(phi_2), amp_2, 'x', mew=3, markersize=16, label="Messwerte")
ax2.plot(phi, legend1(phi, *param1),linewidth=4, label="Ausgleichskurve")
ax2.legend()


param2, cov2 = curve_fit(legend2, np.deg2rad(phi_4[8:]), amp_4[8:])
err2 = np.sqrt(np.diag(cov2))
a2 = ufloat(param2[0], err2[0])
print(a2)
#Polarplot 5 kHz
ax3 =fig_10.add_subplot(223, projection='polar')
ax3.plot(np.deg2rad(phi_4), amp_4, 'x', mew=3, markersize=16, label="Messwerte")
ax3.plot(phi, legend2(phi, *param2),linewidth=4, label="Ausgleichskurve")
ax3.legend()

param3, cov3 = curve_fit(legend3, np.deg2rad(phi_3[8:]), amp_3[8:])
err3 = np.sqrt(np.diag(cov3))
a3 = ufloat(param3[0], err3[0])
print(a3)
#Polarplot 7,4kHz
ax4 =fig_10.add_subplot(224, projection='polar')
ax4.plot(np.deg2rad(phi_3), amp_3, 'x', mew=3, markersize=16, label="Messwerte")
ax4.plot(phi, legend3(phi, *param3),linewidth=4, label="Ausgleichskurve")
ax4.legend()
plt.savefig("plots/C_polar1.pdf")

#180° mit Zwischenring (Dicke h=3mm/h=6mm/h=9mm)
fig_14 = plt.figure(figsize=(12,20))
ax1 = fig_14.add_subplot(311)
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_c4_1*1e-3, amp_c4_1, linewidth=4, label="3 mm")
ax1.grid()
ax1.legend()
ax2 = fig_14.add_subplot(312)
ax2.set_ylabel(r"Amplitude / (a.u.)")
ax2.plot(f_c4_2*1e-3, amp_c4_2, linewidth=4, label="6 mm")
ax2.grid()
ax2.legend()
ax3 = fig_14.add_subplot(313)
ax3.set_xlabel(r"$f$ / kHz")
ax3.set_ylabel(r"Amplitude / (a.u.)")
ax3.plot(f_c4_3*1e-3, amp_c4_3, linewidth=4, label="9 mm")
ax3.grid()
ax3.legend()
plt.savefig("plots/C_4.pdf")

#Aufspaltung gegen Ringdicke
fig_15 = plt.figure(figsize=(15,8))
ax1 = fig_15.add_subplot(111)
ax1.set_xlabel(r"Ringdicke / mm")
ax1.set_ylabel(r"Aufspaltung / Hz")
ax1.plot(dicke, aufspaltung, 'x', mew=3, markersize=16, label="Messwerte")
ax1.grid()
ax1.legend()
plt.savefig("plots/C_Aufspaltung.pdf")

#Polarplot 2,3kHz mit Zwischenring
def legend5(phi, a):
    return np.abs(a*(1-np.cos(phi)**2)**(0.5) )

param5, cov5 = curve_fit(legend1, np.deg2rad(phi_5), amp_5)
err5 = np.sqrt(np.diag(cov5))
a5 = ufloat(param5[0], err5[0])
print(a5)

param5_1, cov5_1 = curve_fit(legend0, np.deg2rad(phi_5), amp_5_1)
err5_1 = np.sqrt(np.diag(cov5_1))
a5_1 = ufloat(param5_1[0], err5_1[0])
print(a5_1)

fig_16 = plt.figure(figsize=(25,12.5))
ax1 =fig_16.add_subplot(121, projection='polar')
ax1.plot(np.deg2rad(phi_5), amp_5_1, 'x', mew=3, markersize=16, label="Messwerte")
ax1.plot(phi, legend0(phi, *param5_1),linewidth=4, label="Ausgleichskurve")
ax1.legend()
ax2 =fig_16.add_subplot(122, projection='polar')
ax2.plot(np.deg2rad(phi_5), amp_5, 'x', mew=3, markersize=16, label="Messwerte")
ax2.plot(phi, legend1(phi, *param5),linewidth=4, label="Ausgleichskurve")
ax2.legend()
plt.savefig("plots/C_polar5.pdf")


#D
#Zwei Kugeln, 180°, ohne Blende und mit Blende (d=10mm/d=13mm/d=16mm)
fig_17 = plt.figure(figsize=(15, 24))
ax1 = fig_17.add_subplot(411)
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_d1_1*1e-3, amp_d1_1, linewidth=4, label="Keine Blende" )
ax1.grid()
ax1.legend()
ax2 = fig_17.add_subplot(412)
ax2.set_ylabel(r"Amplitude / (a.u.)")
ax2.plot(f_d1_2*1e-3, amp_d1_2,linewidth=4, label="10 mm Blende")
ax2.grid()
ax2.legend()
ax3 = fig_17.add_subplot(413)
ax3.set_ylabel(r"Amplitude / (a.u.)")
ax3.plot(f_d1_3*1e-3, amp_d1_3,linewidth=4, label="13 mm Blende")
ax3.grid()
ax3.legend()
ax4 = fig_17.add_subplot(414)
ax4.set_xlabel(r"$f$ / kHz")
ax4.set_ylabel(r"Amplitude / (a.u.)")
ax4.plot(f_d1_4*1e-3, amp_d1_4,linewidth=4, label="16 mm Blende")
ax4.grid()
ax4.legend()
plt.savefig("plots/D_1.pdf")

#Resonanzfreq. gegen Blendendurchmesser
fig_18 = plt.figure(figsize=(15,8))
ax1 = fig_18.add_subplot(111)
ax1.set_xlabel(r"Blendendurchmesser / mm")
ax1.set_ylabel(r"Resonanzfrequenz / kHz")
ax1.plot(durchmesser, frequenz1, 'x', mew=3, markersize=16, label="1. Resonanz")
ax1.plot(durchmesser, frequenz2, 'x', mew=3, markersize=16, label="2. Resonanz")
ax1.plot(durchmesser, frequenz3, 'x', mew=3, markersize=16, label="3. Resonanz")
ax1.grid()
ax1.legend()
plt.savefig("plots/D_2.pdf")

#Polarplot 2,3kHz & Blende
fig_19 = plt.figure(figsize=(15,15))
fig_19.add_subplot(111, projection='polar')
plt.polar(np.deg2rad(phi_6), amp_6, 'x', mew=3, markersize=16, label="Messwerte")
plt.legend()
plt.savefig("plots/D_3.pdf")


#Molekuel, bei 180 Grad
f_d3_1, amp_d3_1 = np.genfromtxt("data/d_3_1.dat", unpack=True)
f_d3_2, amp_d3_2 = np.genfromtxt("data/d_3_2.dat", unpack=True)

fig_20 = plt.figure(figsize=(15,8))
ax1 = fig_20.add_subplot(111)
ax1.set_xlabel(r"$f$ / kHz")
ax1.set_ylabel(r"Amplitude / (a.u.)")
ax1.plot(f_d3_1*1e-3, amp_d3_1, linewidth=4, label="Obere Kugel")
ax1.plot(f_d3_2*1e-3, amp_d3_2, linewidth=4, label="Untere Kugel")
ax1.grid()
ax1.legend()
plt.savefig("plots/D_phase.pdf")

#save solution
#file = open("plots/solution.txt", "w")
#file.write("Hallo")
#file.close()

