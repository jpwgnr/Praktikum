import numpy as np 
import uncertainties.unumpy as unp

phi_data,F_data= np.genfromtxt("D.txt", unpack=True)
r= unp.uarray(0.259,0.0005) #extend to an array of the length of F and phi
F=unp.uarray(F_data, 0)
phi= unp.uarray(phi_data, 0) *2*np.pi/360

D=( F*r)/phi

D_mittel=sum(D)/len(D)
print("Einzelwerte von D:", D, "\n Mittelwert von D: ", D_mittel ) #Mittelwert D
file = open("ErgebnisD.txt", "w")
file.write("Einzelwerte von D: {} \n Mittelwert von D: {} ".format(D, D_mittel))
file.close()
