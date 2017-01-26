import DMprofiles as DM # first import
import imp
imp.reload(DM)
import numpy as np
import matplotlib.pyplot as plt
import pandas  as pd  

 
                

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
 
R0 = 8. # Sun's galactocentric distance
Rs = 20. # Scale Radius gNFW profile
          
 
greenorange12 = [(50, 162, 81), (172, 217, 141), (255, 127, 15), (255, 185, 119), 
                (60, 183, 204), (152, 217, 228), (184, 90, 13), (255, 217, 74), 
                (57, 115, 124), (134, 180, 169), (130, 133, 59), (204, 201, 77)]

colorpalette = greenorange12

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(colorpalette)):    
    r, g, b = colorpalette[i]    
    colorpalette[i] = (r / 255., g / 255., b / 255.)
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#gNFW1 = DM.gNFW(R0, 0.49, Rs, 0.45)
gNFW1 = DM.gNFW(R0, 0., 4.8, 0.36)
gNFW2 = DM.gNFW(R0, 1.28, Rs, 0.32)
#gNFW3 = DM.gNFW(R0, 0.048, 5.15, 0.317)



with open('/Users/maria/Desktop/RESULTS FROM CLUSTER/R8/BULGE/I/E2bulge_rcI.dat', 'r') as g:
    next(g); next(g) 
    vB=[]; rB=[]
    for line in g:
        Data=line.split()
        if line.startswith('#'):
                continue
        try:
            vB.append(float(Data[0])); rB.append(float(Data[2])); 
        except IndexError:
            print Data
with open('/Users/maria/Desktop/RESULTS FROM CLUSTER/R8/DISC/BRdisc_rc.dat', 'r') as g:
    next(g); next(g)
    vI=[]; rI=[]
    for line in g:
        if line.startswith('#'):
                continue
        Data=line.split()
        try:
            vI.append(float(Data[0])); rI.append(float(Data[2])); 
        except IndexError:
            print Data
with open('/Users/maria/Desktop/RESULTS FROM CLUSTER/GAS/Ferriere9807.dat', 'r') as g:
        next(g); next(g);
        vX=[]; rX=[]
        for line in g:
            if line.startswith('#'):
                continue
            Data=line.split()
            try:
                vX.append(float(Data[0])); rX.append(float(Data[6])); 
            except IndexError:
                print Data

vBiX = []
vBiX_NFW1 = [];  vBiX_NFW2 = [];
#vBiX_NFW3 = []

if len(vB)==len(vI) and len(vI)==len(vX):
    print "lenght of Bulge, disc and gas are equal"
else:
    exit


v1 = gNFW1.velocity(rB)
v2 = gNFW2.velocity(rB)
#v3 = gNFW3.velocity(rB)

for j in range(len(rB)):
    vBiX.append(np.sqrt(vB[j]**2+vI[j]**2+vX[j]**2))
    vBiX_NFW1.append(np.sqrt(vBiX[j]**2+v1[j]**2))
    vBiX_NFW2.append(np.sqrt(vBiX[j]**2+v2[j]**2))
    #vBiX_NFW3.append(np.sqrt(vBiX[j]**2+v3[j]**2))


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

filenameGalkin = '/Users/maria/Desktop/RESULTS FROM CLUSTER/observations/vcdataWOoutliersR8v230.dat'
columnsGalkin = ['radio', 'deltaRadio', 'velocity', 'deltaVelocity', 'w', 'deltaw', 'reference']  
filenameGalkinHalo = '/Users/maria/Dropbox/MWRC/data/binned_inn_out.dat'    
 
df = pd.read_csv(filenameGalkin, # filename
                    sep='\s+', # whitespace separates the columns 
                    skiprows=[0] and [1], # skip the first and second row
                    header = None, # no header files to read 
                    names = columnsGalkin) # header files
                    
df1 = pd.read_csv(filenameGalkinHalo, # filename
                    sep='\s+', # whitespace separates the columns 
                    header = None, # no header files to read 
                    names = ['radio', 'velocity', 'deltaVelocity']) # header files
                              
plt.figure(figsize=(12, 9))
    
 
#plt.errorbar(df.radio, df.velocity, yerr=df.deltaVelocity, 
#             fmt='+', color=colorpalette[1], label='Galkin dataset')


plt.errorbar(df1.radio, df1.velocity, yerr=df1.deltaVelocity, 
             fmt='o',  capthick=3, elinewidth=3, color=colorpalette[2],
             label='Galkin + Halo Stars') 

plt.plot(rB, vBiX_NFW1, 
             linewidth=2.5, color=colorpalette[4], label='$ \gamma=0, R_s=4.8 $') 
                
plt.plot(rB, vBiX_NFW2, 
             linewidth=2.5, color=colorpalette[5], label='$ \gamma=1.28, R_s=20 $')
                                                                                                      
# Limit the range of the plot
plt.ylim(50, 450)    
plt.xlim(0, 50)

# Write text in the plot 
#plt.text(12, 70, 'text starting at (12,70)', fontsize=26)

# Set ticks properties          
plt.xticks(range(0, 55, 5))
plt.tick_params(axis='both', labelsize=24) 

# Set axis labels
plt.ylabel("$\mathrm{ v \; [km/s]} $"); 
plt.xlabel('R [kpc]');
    
# Set default font family and size
plt.rc('font', family='serif', serif='cmr10', size=32)
    
# Set legend 
plt.legend(frameon=False, prop={'size':20}, ncol=2, loc=2)
 
# Set grid      
plt.grid()  
     
plt.show()  
# Finally, save the figure as a PNG.    
# You can also save it as a PDF, JPEG, etc. Just change the file extension in this call.    
# bbox_inches="tight" removes all the extra whitespace on the edges of your plot.    
plt.savefig('RCgalkin+haloStars.png', bbox_inches='tight')    
          




