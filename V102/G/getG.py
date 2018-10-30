import numpy as np 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
#variables

mk= ufloat(512.2e-3, 512.2e-3*0.04e-2) #kg
Rk= ufloat(25.38e-3, 50.76e-3*0.007e-2) #m
theta= ufloat(22.5e-7,0)
def functionG(T, mk, Rk, L, R):
   return (8*np.pi*L*(mk*(2/5)*(Rk**2)+theta))/((T**2)*(R**4))

# T in s 
data_T=np.genfromtxt("valuesT.txt", unpack= True)
# L in cm transform to m
data_L=np.genfromtxt("valuesL.txt", unpack= True)*1e-2
# d in micrometer transform to meter
data_d=np.genfromtxt("valuesd.txt", unpack= True)*1e-3

#Average of T 
T= ufloat(np.mean(data_T), np.std(data_T)) 
#Average of L
L= ufloat(np.mean(data_L), np.std(data_L)) 
#Average of d 
d= ufloat(np.mean(data_d), np.std(data_d))  
#
G= functionG(T, mk, Rk, L, d/2)


file = open("ErgebnisG.txt", "w")

file.write("Average of T: {} \n Average of L: {} \n Average of d= {} \n Value G: {}".format(T, L, d, G))

#Experimentalwert: 9,5 +-0.5 
#Literaturwert: 79,3 GPa [1e9 kg/(m*s²)]
file.close()


