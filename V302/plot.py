import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
#a
R3a, R4a, R2a_var = np.genfromtxt("data/dataa.txt", unpack=True)
taba = TexTable([R3a,R4a,R2a_var], [r"$R3/\si{\ohm}$", r"$R4/\si{\ohm}$", r"$R2/\si{\ohm}$"], label="taba", caption=" Die verschiedenen Werte der bekannten Widerstände der Wheatstoneschen Brücke.", roundPrecision=0)
taba.writeFile("build/taba.tex")
#b 
R3b, R2b, R4b, C2b_var = np.genfromtxt("data/datab.txt", unpack=True)
tabb = TexTable([R3b, R2b, R4b, C2b_var*1e9], [r"$R3/\si{\ohm}$", r"$R2/\si{\ohm}$", r"$R4/\si{\ohm}$", r"$C2/\si{\nano\farad}$"], label="tabb", caption="Die verschiedenen Werte der Widerstände und Kapazitäten einer Kapazitätsmessbrücke. ", roundPrecision=0)
tabb.writeFile("build/tabb.tex")
#c 
R3c, R2c, R4c, L2c_var = np.genfromtxt("data/datac.txt", unpack=True)
tabc = TexTable([R3c, R2c, R3c, L2c_var*1e3], [r"$R3/\si{\ohm}$", r"$R2/\si{\ohm}$", r"$R4/\si{\ohm}$", r"$L2/\si{\milli\henry$}"], label="tabc", caption="Die verschiedenen Werte der Widerstände und der  Spule einer Induktivitätsmessbrücke.", roundPrecision=0)
tabc.writeFile("build/tabc.tex")
#d 
R3d, R4d = np.genfromtxt("data/datad.txt", unpack=True)
tabd = TexTable([R3d,R4d], [r"$R3/\si{ohm}$", r"$R4/\si{\ohm}$"], label="tabd", caption="Die verschiedenen Widerstände für eine Maxwell-Brücke.", roundPrecision=0)
tabd.writeFile("build/tabd.tex")
#e
fe, U_Brezwei = np.genfromtxt("data/datae.txt", unpack=True)
tabe = TexTable([fe,U_Brezwei], [r"$f/\si{\Hz}$", r"$2 U_{Br}/\si{\V}$"], label="tabe", caption="Die Frequenz gegen den doppelten Wert der Amplitude der Brückenspannung.", roundPrecision=3)
tabe.writeFile("build/tabe.tex")
#extra values 
#a 
R2a= unp.uarray(R2a_var, R2a_var*0.0002)
#b 
C2b= unp.uarray(C2b_var, C2b_var*0.0002)
#c 
L2c= unp.uarray(L2c_var, L2c_var*0.0002)
#d 
R2d_var= 1000  
R2d= ufloat(R2d_var, R2d_var*0.0002)
C4d_var= 992e-9 
C4d= ufloat(C4d_var, C4d_var*0.0002)
#e 
R_extrae= 332 
Re= 1000
Ce= 420e-9 
U_Se = 2.5
U_Bre = U_Brezwei/2 
omega0etheo= 1/(Re*Ce)
omega0e= 400*2*np.pi
omegae= 2*np.pi*fe
#functions 
#a 
def getRx(R2, R3, R4):
    return R2*(R3/R4)
#b 
def getCxb(C2, R4, R3):
    return C2*(R4/R3)
#c 
def getLxc(L2, R3, R4):
    return L2*(R3/R4)
#d 
def getLxd(C4, R3, R4): 
    return C4*R3*R4 
#e 
def getU_Br(omega, R, C):
    return np.sqrt(np.abs((((omega**2)*(R**2)*(C**2)-1)**2)/(9*(((1-(omega**2)*(R**2)*(C**2))**2)+(9*(omega**2)*(R**2)*(C**2))))))

#def function(x, a, b, c, d, U_S):
#     return a * np.sin(b * x + c) + d
#calculate 
#a 
val_Rxa1= getRx(unp.nominal_values(R2a[0:3]), R3a[0:3], R4a[0:3])
Rxa1= ufloat(val_Rxa1.mean(), val_Rxa1.std()) 
val_Rxa2= getRx(unp.nominal_values(R2a[3:6]), R3a[3:6], R4a[3:6])
Rxa2= ufloat(val_Rxa2.mean(), val_Rxa2.std()) 
#b
val_Rxb= getRx(R2b, R3b, R4b)
Rxb= ufloat(val_Rxb.mean(), val_Rxb.std()) 
val_Cxb= getCxb(unp.nominal_values(C2b), R4b, R3b)
Cxb= ufloat(val_Cxb.mean(), val_Cxb.std()) 
#c
val_Rxc= getRx(R2c, R3c, R4c)
Rxc= ufloat(val_Rxc.mean(), val_Rxc.std()) 
val_Lxc= getLxc(unp.nominal_values(L2c), R3c, R4c)
Lxc= ufloat(val_Lxc.mean(), val_Lxc.std()) 
#d
val_Rxd= getRx(R2d.nominal_value, R3d, R4d)
Rxd= ufloat(val_Rxd.mean(), val_Rxd.std()) 
val_Lxd= getLxd(C4d.nominal_value, R3d, R4d)
Lxd= ufloat(val_Lxd.mean(), val_Lxd.std()) 
#e
tab1 = TexTable([omegae,U_Bre/U_Se], [r"$omega\/\si[per-mode=fraction]{\per\second}$", r"$\frac{U_{Br}}{U_S}$"], label="tab1", caption="Die Kreisfrequenz gegen das Verhältnis aus Brückenpannung durch Speisespannung.", roundPrecision=3)
tabe.writeFile("build/tab1.tex")
#f 
k= (1/U_Se)*(60.8e-3/0.149)
#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
 
parameters, pcov = curve_fit(getU_Br, omegae[0:17], U_Bre[0:17]/U_Se, p0=(Re,Ce))

#save solution 

file = open("build/solution.txt", "w")
file.write("a)\n\tRx1= {} Ohm\n\t Rx2= {} Ohm\n\nb)\n\tRx= {} Ohm\n\tCx= {} Farad\n\nc)\n\tRx= {} Ohm\n\tLx= {} Henry\n\nd)\n\tRx= {} Ohm\n\tLx= {} Henry\n\nOmega0= 1/RC = {} \n\nOmega0_exp= {}\n\nf)\n\tKlirrfaktor k= {}".format(Rxa1, Rxa2, Rxb, Cxb, Rxc, Lxc, Rxd, Lxd, omega0etheo, omega0e, k))
file.close()

#Make plots for data
#theoriekurve 
newomega=np.linspace(omegae[0], omegae[-1], 2000)
theoU_Br=getU_Br(newomega, Re, Ce)

plt.figure(1)
plt.plot(omegae/omega0e, U_Bre/U_Se, "xr", label="Daten")
plt.plot(newomega/omega0e, getU_Br(newomega, *parameters), "r", label="Fit", linewidth=1.0)
plt.plot(newomega/omega0e, theoU_Br, "b", label="Theoriekurve", linewidth=1.0)
plt.xlabel(r"$\frac{\omega}{\omega_0}$")
plt.ylabel(r"$\frac{U_{Br}}{U_S}$")
plt.xscale("log")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#curvefit plot

#plt.errorbar(x, y, yerr=err_y, fmt='rx', label='Daten')
#t = np.linspace(-0.5, 2 * np.pi + 0.5)
#plt.plot(t, f(t, *parameters), 'b-', label='Fit')
#plt.plot(t, np.sin(t), 'g--', label='Original')
#plt.xlim(t[0], t[-1])
#plt.xlabel(r'$t$')
#plt.ylabel(r'$f(t)$')
#plt.legend(loc='best')
#plt.tight_layout()
#plt.savefig("build/plot1b.pdf")

