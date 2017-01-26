# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# Plot different radial DM density profiles : 
# (1) Isothermal - something strange with the RC
# (2) NFW
# (3) DC14 - I SHOULD STUDY THIS IN DETAIL, SINCE SFR AND RHO0 ARE CORRELATED
#            (this is what Ekaterina said)
#
# 
# Conversion factors:
#
#   G=1.18997e-31 cm³/GeV s²
#   1 kpc = 3.08567758e16 km 
#
#-------------------------------------------------------------------------------

#import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy.integrate

class isothermal:
    
    def __init__(self, R0, rho0, Rc):#, R):
        " rho0  is the local DM density "
        " rhoC  is the central DM density in GeV/cm^3 "
        " Rc is the core radius "
        self.R0 = R0
        self.rho0 = rho0
        self.rhoC = rho0*(1+(self.R0/Rc)**2)
        self.Rc = Rc
        #self.R = R
        self.R = np.arange(0.2, 55, 0.5)
    

    def plotDensity(self, ax):
        rho = [];
        for r in self.R:
            rho.append(self.rhoC/(1+(r/self.Rc)**2))
            
        ax.plot(self.R, rho, linewidth = 2., \
                label =r'$ isothermal:\;R_c=$'+str(self.Rc)+r'$ Kpc,\;\rho_0=$'+str(self.rho0)+r'$ GeV/cm^3 $')
        ax.set_yscale('log'); ax.set_xscale('log')
        ax.legend(frameon=False, prop={'size':16}, loc=0, ncol=1) # I do not know if I should write this set legend outside!!!
        ax.set_ylabel(r"$ \rho \; \mathrm{[GeV/cm^3]} $", size=20); 
        ax.set_xlabel("$ r\; \mathrm{[kpc]} $", size=20);
        
    def plotVelocity(self, ax):
        v = []
        for Rint in self.R:
            rho = lambda r, rhoC, Rc:4*m.pi*r**2*rhoC/(1+(r/Rc)**2)
            Integral = scipy.integrate.quad(rho, 0, Rint, args=(self.rhoC, self.Rc,))
            v.append(m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16)) 
       
        ax.plot(self.R, v, linewidth = 2., \
                label =r'$ isothermal:\;R_c=$'+str(self.Rc)+r'$ Kpc,\;\rho_0=$'+str(self.rho0)+r'$ GeV/cm^3 $')
        ax.legend(frameon=False, prop={'size':16}, loc=0, ncol=1) # I do not know if I should write this set legend outside!!!
        ax.set_ylabel(r"$ v \; \mathrm{[km/s]} $", size=20); 
        ax.set_xlabel("$ r\;\mathrm{[kpc]} $", size=20);  
    
    def velocity(self):
         v = []
         for Rint in self.R:
            rho = lambda r, rhoC, Rc:4*m.pi*r**2*rhoC/(1+(r/Rc)**2)
            Integral = scipy.integrate.quad(rho, 0, Rint, args=(self.rhoC, self.Rc,))
            v.append(m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16)) 
         return v 

class Burkert:
    " An empirical law that resembles the isohtermal halo "
    def __init__(self, R0, rho0, Rc):#, R):
        self.R0 = R0
        self.rho0 = rho0
        self.rhoC = rho0*(R0+Rc)*(R0**2+Rc**2)/Rc**3
        self.Rc = Rc
        #self.R = R
        self.R = np.arange(0.1, 50, 0.5)
    
    def plotDensity(self, ax):
        rho = []
        for r in self.R:
            rho.append(self.rhoC*self.Rc**3/((r+self.Rc)*(r**2+self.Rc**2)))
        ax.plot(self.R, rho, linewidth = 2., \
                label =r'$ Burkert:\;R_c=$'+str(self.Rc)+r'$ Kpc,\;\rho_0=$'+str(self.rho0)+r'$ GeV/cm^3 $')
        ax.set_yscale('log'); ax.set_xscale('log')
        ax.legend(frameon=False, prop={'size':16}, loc=0, ncol=1) # I do not know if I should write this set legend outside!!!
        ax.set_ylabel(r"$ \rho \; \mathrm{[GeV/cm^3]} $", size=20); 
        ax.set_xlabel("$ r\; \mathrm{[kpc]} $", size=20);
        
    def plotVelocity(self, ax):
        "Need to implement"

    def velocity(self, R):
         v = []
         for Rint in R:
            rho = lambda r, rhoC, Rc:4*m.pi*r**2*rhoC*Rc**3/((r+Rc)*(r**2+Rc**2))
            Integral = scipy.integrate.quad(rho, 0, Rint, args=(self.rhoC, self.Rc,))
            v.append(m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16)) 
         return v 

class gNFW:
    
    def __init__(self, R0, gamma, Rs, rho0):#, R):
        " gamma is the inner slope "
        " Rs is the scale radius "
        " rho0 is the local DM density (DM density at the Sun's position) "
        self.gamma = gamma
        self.Rs = Rs
        self.rho0 = rho0
        self.R0 = R0 # Sun's galactocentric distance
        #self.R = R
        self.R = np.arange(0.1, 50, 0.5)
    
        
    def plotDensity(self, ax):
        rho = []
        for r in self.R:
            rho.append(self.rho0*(self.R0/r)**self.gamma*((self.Rs+self.R0)/(self.Rs+r))**(3-self.gamma))
            
        ax.plot(self.R, rho, linewidth = 2., \
                label =r'$ gNFW:\;\gamma=$'+str(self.gamma)+ \
                r'$,\;\rho_0=$'+str(self.rho0)+r'$ GeV/cm^3,\;R_s=$'+ str(self.Rs)+' kpc')
        ax.set_yscale('log'); ax.set_xscale('log')
        ax.legend(frameon=False, prop={'size':16}, loc=0, ncol=1) 
        ax.set_ylabel(r"$ \rho \; \mathrm{[GeV/cm^3]} $", size=20); 
        ax.set_xlabel("$ r\; \mathrm{[kpc]} $", size=20);
        
    def velocity(self, R):
        v  = []
        for Rint in R:
            rho = lambda r, gamma, Rs, rho0, R0:4*m.pi*r**2*rho0*(R0/r)**gamma*((Rs+R0)/(Rs+r))**(3-gamma)
            Integral = scipy.integrate.quad(rho, 0, Rint, args=(self.gamma,self.Rs,self.rho0,self.R0,))
            v.append(m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16))
            print Rint, "  ", m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16)
        return v
    
    def plotVelocity(self, ax):
        v = []
        for Rint in self.R:
            rho = lambda r, gamma, Rs, rho0, R0:4*m.pi*r**2*rho0*(R0/r)**gamma*((Rs+R0)/(Rs+r))**(3-gamma)
            Integral = scipy.integrate.quad(rho, 0, Rint, args=(self.gamma,self.Rs,self.rho0,self.R0,))
            v.append(m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16))
       
        ax.plot(self.R, v, label =r'$ gNFW:\;\gamma=$'+str(self.gamma)+ \
                r'$,\;\rho_0=$'+str(self.rho0)+r'$ GeV/cm^3,\;R_s=$'+ str(self.Rs)+' kpc')
        ax.legend(frameon=False, prop={'size':16}, loc=0, ncol=1) 
        ax.set_ylabel(r"$ v \;\mathrm{[km/s]} $", size=20); 
        ax.set_xlabel("$ r\;\mathrm{[kpc]} $", size=20);     
            
class DC14:
    
    def __init__(self, R0, Rs, rho0, SFR):
        self.R0 = R0
        self.Rs = Rs
        self.rho0 = rho0
        self.SFR = SFR
        self.x = m.log10(SFR)
        self.alpha = 2.94 - m.log10((10**(self.x+2.33))**(-1.08) + (10**(self.x+2.33))**(2.29))
        self.beta = 4.23 + 1.34*self.x + 0.26*self.x**2
        self.gamma = -0.06 + m.log10((10**(self.x+2.56))**(-0.68)+10**(self.x+2.56))
        self.rhoS=self.rho0*((self.R0/self.Rs)**self.gamma)* \
                ((1+(self.R0/self.Rs)**self.alpha)**((self.beta-self.gamma)/self.alpha)) #GeV/cm^3
#    rhoS=self.rhoS*(3.08567*10**21)**3 #change to GeV/Kpc
        
        self.R = np.arange(0.1, 50, 0.5)
        
        
    def plotDensity(self, ax):
        rho = []
        for r in self.R:
            rho.append(self.rhoS/((r/self.Rs)**self.gamma* \
                    ((1+(r/self.Rs)**self.alpha)**((self.beta-self.gamma)/self.alpha))))
        ax.plot(self.R, rho, label =r'$ DC14:\;\SFR=$'+str(self.SFR)+ \
                r'$,\;\rho_0=$'+str(self.rho0)+r'$ GeV/cm^3,\;R_s=$'+ str(self.Rs)+' kpc')
        ax.set_yscale('log'); ax.set_xscale('log')
        ax.legend(frameon=False, prop={'size':16}, loc=0, ncol=1) 
        ax.set_ylabel(r"$ \rho \; \mathrm{[GeV/cm^3]} $", size=20); 
        ax.set_xlabel("$ r\; \mathrm{[kpc]} $", size=20);
    
    def plotVelocity(self, ax):
        "Need to implement"
        
Rint = 5. ; gamma = 1.; R0 = 8.; rho0 = 0.4; Rs = 20.;
rho = lambda r, gamma, Rs, rho0, R0:4*m.pi*r**2*rho0*(R0/r)**gamma*((Rs+R0)/(Rs+r))**(3-gamma)
Integral = scipy.integrate.quad(rho, 0, Rint, args=(gamma, Rs, rho0, R0,))
v = (m.sqrt(1.18997*10**(-31)*Integral[0]/Rint)*3.08567758*10**(16))

print v