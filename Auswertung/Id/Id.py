import numpy as np
import uncertainties.unumpy as unp

#Daten T und A zum Quadrat
dist_data, T_data= np.genfromtxt("Id.txt", unpack=True)
err_a=np.ones(len(dist_data))*0.05
err_T=np.ones(len(T_data))*0.5
a_2=(unp.uarray(dist_data, err_a)/100)**2
T_2=(unp.uarray(T_data, err_T)/10)**2

np.savetxt("ErgebnisA.txt", a_2, fmt="%r")
np.savetxt("ErgebnisT.txt", T_2, fmt="%r")

#Id berechnen:

y_absch=unp.uarray(3.5,0) #s²

#I1 und I2:
m1=unp.uarray(0.22316,0) 
m2=unp.uarray(0.22224,0) 

d1=unp.uarray(0.035, 0.00005)


I1= 0.5* m1 *(d1**2)
I2= 0.5* m2 *(d1**2)
#D aus ErgebnisD
D= unp.uarray(0.014088, 0.000027)

Id= y_absch*D/(4*np.pi**2) -I1 -I2 
file= open("ErgebnisId.txt", "w")
file.write("Y-Abschnitt: {} \n Trägheitsmoment m1= {} \n Trägheitsmoment m2= {} \n Winkelrichtgröße D= {} \n Trägheitsmoment Id= {}".format(y_absch, I1, I2, D, Id))
file.close()
