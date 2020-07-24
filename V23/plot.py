import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
#from something import some 

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
phi_5, amp_5 = np.genfromtxt("data2/polar_atom5.txt", unpack=True)


#D) H-Molekuel
#Zwei Kugeln, 180°, ohne Blende
f_d1_1, amp_d1_1 = np.genfromtxt("data/d_1_1.dat", unpack=True)

#Zwei Kugeln, 180°, mit Blende (d=10mm/d=13mm/d=16mm)
f_d1_2, amp_d1_2 = np.genfromtxt("data/d_1_2.dat", unpack=True)
f_d1_3, amp_d1_3 = np.genfromtxt("data/d_1_3.dat", unpack=True)
f_d1_4, amp_d1_4 = np.genfromtxt("data/d_1_4.dat", unpack=True)

#Resonanzfreq. gegen Blendendurchmesser
durchmesser, frequenz = np.genfromtxt("data2/resonanzen.txt", unpack=True)

#selbst abgelesen bei 2,3kHz & Blende: Winkel und Maximum Amplitude
phi_6, amp_6 = np.genfromtxt("data2/polar_molekuel.txt", unpack=True)



#Plots erstellen

#A
#1 bis 12 Zylinder (l=50mm)
fig_1 = plt.figure(figsize=(8,14))
ax1 = fig_1.add_subplot(6,2,1)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_a2_1*1e-3, amp_a2_1);
ax2 = fig_1.add_subplot(6,2,2)
#ax2.set_xlabel(r"$f$/kHz")
#ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_a2_2*1e-3, amp_a2_2);
ax3 = fig_1.add_subplot(6,2,3)
#ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_a2_3*1e-3, amp_a2_3);
ax4 = fig_1.add_subplot(6,2,4)
#ax4.set_xlabel(r"$f$/kHz")
#ax4.set_ylabel(r"Amplitude/ (a.u.)")
ax4.plot(f_a2_4*1e-3, amp_a2_4);
ax5 = fig_1.add_subplot(6,2,5)
#ax5.set_xlabel(r"$f$/kHz")
ax5.set_ylabel(r"Amplitude/ (a.u.)")
ax5.plot(f_a2_5*1e-3, amp_a2_5);
ax6 = fig_1.add_subplot(6,2,6)
#ax6.set_xlabel(r"$f$/kHz")
#ax6.set_ylabel(r"Amplitude/ (a.u.)")
ax6.plot(f_a2_6*1e-3, amp_a2_6);
ax7 = fig_1.add_subplot(6,2,7)
#ax7.set_xlabel(r"$f$/kHz")
ax7.set_ylabel(r"Amplitude/ (a.u.)")
ax7.plot(f_a2_7*1e-3, amp_a2_7);
ax8 = fig_1.add_subplot(6,2,8)
#ax8.set_xlabel(r"$f$/kHz")
#ax8.set_ylabel(r"Amplitude/ (a.u.)")
ax8.plot(f_a2_8*1e-3, amp_a2_8);
ax9 = fig_1.add_subplot(6,2,9)
#ax9.set_xlabel(r"$f$/kHz")
ax9.set_ylabel(r"Amplitude/ (a.u.)")
ax9.plot(f_a2_9*1e-3, amp_a2_9);
ax10 = fig_1.add_subplot(6,2,10)
#ax10.set_xlabel(r"$f$/kHz")
#ax10.set_ylabel(r"Amplitude/ (a.u.)")
ax10.plot(f_a2_10*1e-3, amp_a2_10);
ax11 = fig_1.add_subplot(6,2,11)
ax11.set_xlabel(r"$f$/kHz")
ax11.set_ylabel(r"Amplitude/ (a.u.)")
ax11.plot(f_a2_11*1e-3, amp_a2_11);
ax12 = fig_1.add_subplot(6,2,12)
ax12.set_xlabel(r"$f$/kHz")
#ax12.set_ylabel(r"Amplitude/ (a.u.)")
ax12.plot(f_a2_12*1e-3, amp_a2_12);
plt.savefig("plots/A_2.pdf")

#1 Zylinder (l=75mm)
fig_2 = plt.figure(figsize=(8,7))
ax1 = fig_2.add_subplot(111)
ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_a3*1e-3, amp_a3)
plt.savefig("plots/A_3.pdf")


#B
#2 bis 10 Zylinder (l=50mm), 1 bis 9 Blenden (d=16mm)
fig_3 = plt.figure(figsize=(8,21))
ax1 = fig_3.add_subplot(9,1,1)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b1_2*1e-3, amp_b1_2);
ax2 = fig_3.add_subplot(9,1,2)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_b1_3*1e-3, amp_b1_3);
ax3 = fig_3.add_subplot(9,1,3)
#ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_b1_4*1e-3, amp_b1_4);
ax4 = fig_3.add_subplot(9,1,4)
#ax4.set_xlabel(r"$f$/kHz")
ax4.set_ylabel(r"Amplitude/ (a.u.)")
ax4.plot(f_b1_5*1e-3, amp_b1_5);
ax5 = fig_3.add_subplot(9,1,5)
#ax5.set_xlabel(r"$f$/kHz")
ax5.set_ylabel(r"Amplitude/ (a.u.)")
ax5.plot(f_b1_6*1e-3, amp_b1_6);
ax6 = fig_3.add_subplot(9,1,6)
#ax6.set_xlabel(r"$f$/kHz")
ax6.set_ylabel(r"Amplitude/ (a.u.)")
ax6.plot(f_b1_7*1e-3, amp_b1_7);
ax7 = fig_3.add_subplot(9,1,7)
#ax7.set_xlabel(r"$f$/kHz")
ax7.set_ylabel(r"Amplitude/ (a.u.)")
ax7.plot(f_b1_8*1e-3, amp_b1_8);
ax8 = fig_3.add_subplot(9,1,8)
#ax8.set_xlabel(r"$f$/kHz")
ax8.set_ylabel(r"Amplitude/ (a.u.)")
ax8.plot(f_b1_9*1e-3, amp_b1_9);
ax9 = fig_3.add_subplot(9,1,9)
ax9.set_xlabel(r"$f$/kHz")
ax9.set_ylabel(r"Amplitude/ (a.u.)")
ax9.plot(f_b1_10*1e-3, amp_b1_10);
plt.savefig("plots/B_1.pdf")

#2,4,10 Zylinder (l=50mm), 1,3,9 Blenden (d=10mm)
fig_4 = plt.figure(figsize=(8,7))
ax1 = fig_4.add_subplot(311)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b2_2*1e-3, amp_b2_2);
ax2 = fig_4.add_subplot(312)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_b2_4*1e-3, amp_b2_4);
ax3 = fig_4.add_subplot(313)
ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_b2_10*1e-3, amp_b2_10);
plt.savefig("plots/B_2.pdf")

#2,4,10 Zylinder (l=50mm), 1,3,9 Blenden (d=13mm)
fig_5 = plt.figure(figsize=(8,7))
ax1 = fig_5.add_subplot(311)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b3_2*1e-3, amp_b3_2);
ax2 = fig_5.add_subplot(312)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_b3_4*1e-3, amp_b3_4);
ax3 = fig_5.add_subplot(313)
ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_b3_10*1e-3, amp_b3_10);
plt.savefig("plots/B_3.pdf")

#10 Zylinder: 9x l=50mm, 1x l=75mm(1)/l=37,5mm(2)/l=62,5mm(3)
fig_6 = plt.figure(figsize=(8,7))
ax1 = fig_6.add_subplot(311)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b4_1*1e-3, amp_b4_1);
ax2 = fig_6.add_subplot(312)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_b4_2*1e-3, amp_b4_2);
ax3 = fig_6.add_subplot(313)
ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_b4_3*1e-3, amp_b4_3);
plt.savefig("plots/B_4.pdf")

#10 Zylinder (abwechselnd l=50mm und l=75mm), 9 Blenden (d=16mm) & Vgl ein Zylinder l=50mm und ein Zylinder l=75mm
fig_7 = plt.figure(figsize=(8,7))
ax1 = fig_7.add_subplot(311)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b5*1e-3, amp_b5);
ax2 = fig_7.add_subplot(312)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_a2_1*1e-3, amp_a2_1);
ax3 = fig_7.add_subplot(313)
ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_a3*1e-3, amp_a3);
plt.savefig("plots/B_5.pdf")

#8 Zylinder (l=50mm), 7 Blenden (abwechselnd d=13mm und d=16mm)
fig_8 = plt.figure(figsize=(8,7))
ax1 = fig_8.add_subplot(111)
ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_b6*1e-3, amp_b6)
plt.savefig("plots/B_6.pdf")


#C
#180°
fig_9 = plt.figure(figsize=(8,7))
ax1 = fig_9.add_subplot(111)
ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_c1*1e-3, amp_c1)
plt.savefig("plots/C_1.pdf")

#Polarplot 2,3kHz
fig_10 = plt.figure(figsize=(8,8))
fig_10.add_subplot(111, projection='polar')
plt.polar(phi_1, amp_1, '.')
plt.savefig("plots/C_polar1.pdf")

#Polarplot 3,7kHz
fig_11 = plt.figure(figsize=(8,8))
fig_11.add_subplot(111, projection='polar')
plt.polar(phi_2, amp_2, '.')
plt.savefig("plots/C_polar2.pdf")

#Polarplot 7,4kHz
fig_12 = plt.figure(figsize=(8,8))
fig_12.add_subplot(111, projection='polar')
plt.polar(phi_3, amp_3, '.')
plt.savefig("plots/C_polar3.pdf")

#Polarplot xy kHz
fig_13 = plt.figure(figsize=(8,8))
fig_13.add_subplot(111, projection='polar')
plt.polar(phi_4, amp_4, '.')
plt.savefig("plots/C_polar4.pdf")

#180° mit Zwischenring (Dicke h=3mm/h=6mm/h=9mm)
fig_14 = plt.figure(figsize=(8,7))
ax1 = fig_14.add_subplot(311)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_c4_1*1e-3, amp_c4_1);
ax2 = fig_14.add_subplot(312)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_c4_2*1e-3, amp_c4_2);
ax3 = fig_14.add_subplot(313)
ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_c4_3*1e-3, amp_c4_3);
plt.savefig("plots/C_4.pdf")

#Aufspaltung gegen Ringdicke
fig_15 = plt.figure(figsize=(8,7))
ax1 = fig_15.add_subplot(111)
ax1.set_xlabel(r"Ringdicke/ mm")
ax1.set_ylabel(r"Aufspaltung")
plt.grid()
ax1.plot(dicke, aufspaltung, 'x')
plt.savefig("plots/C_Aufspaltung.pdf")

#Polarplot 2,3kHz mit Zwischenring
fig_16 = plt.figure(figsize=(8,8))
fig_16.add_subplot(111, projection='polar')
plt.polar(phi_5, amp_5, '.')
plt.savefig("plots/C_polar5.pdf")


#D
#Zwei Kugeln, 180°, ohne Blende und mit Blende (d=10mm/d=13mm/d=16mm)
fig_17 = plt.figure(figsize=(8,10))
ax1 = fig_17.add_subplot(411)
#ax1.set_xlabel(r"$f$/kHz")
ax1.set_ylabel(r"Amplitude/ (a.u.)")
ax1.plot(f_d1_1*1e-3, amp_d1_1);
ax2 = fig_17.add_subplot(412)
#ax2.set_xlabel(r"$f$/kHz")
ax2.set_ylabel(r"Amplitude/ (a.u.)")
ax2.plot(f_d1_2*1e-3, amp_d1_2);
ax3 = fig_17.add_subplot(413)
#ax3.set_xlabel(r"$f$/kHz")
ax3.set_ylabel(r"Amplitude/ (a.u.)")
ax3.plot(f_d1_3*1e-3, amp_d1_3);
ax4 = fig_17.add_subplot(414)
ax4.set_xlabel(r"$f$/kHz")
ax4.set_ylabel(r"Amplitude/ (a.u.)")
ax4.plot(f_d1_4*1e-3, amp_d1_4);
plt.savefig("plots/D_1.pdf")

#Resonanzfreq. gegen Blendendurchmesser
fig_18 = plt.figure(figsize=(8,7))
ax1 = fig_18.add_subplot(111)
ax1.set_xlabel(r"Blendendurchmesser/ mm")
ax1.set_ylabel(r"Resonanzfrequenz/ kHz")
plt.grid()
ax1.plot(durchmesser, frequenz, 'x')
plt.savefig("plots/D_2.pdf")

#Polarplot 2,3kHz & Blende
fig_19 = plt.figure(figsize=(8,8))
fig_19.add_subplot(111, projection='polar')
plt.polar(phi_6, amp_6, '.')
plt.savefig("plots/D_3.pdf")



#save solution
#file = open("plots/solution.txt", "w")
#file.write("Hallo")
#file.close()

