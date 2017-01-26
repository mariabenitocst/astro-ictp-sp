import matplotlib.pyplot as plt
import pandas  as pd  

greenorange12 = [(50, 162, 81), (172, 217, 141), (255, 127, 15), (255, 185, 119), 
                (60, 183, 204), (152, 217, 228), (184, 90, 13), (255, 217, 74), 
                (57, 115, 124), (134, 180, 169), (130, 133, 59), (204, 201, 77)] 
                
def plot_xy(filename, headernames):
    """
    2D plot
    """
    # Read the data into a pandas DataFrame  
    rc = pd.read_csv(filename, # filename
                    sep='\s+', # whitespace separates the columns 
                    skiprows=[0], # skip the first row
                    header = None, # no header files to read 
                    names = headernames) # header files
   
    colorpalette = greenorange12 

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
    for i in range(len(colorpalette)):    
        r, g, b = colorpalette[i]    
        colorpalette[i] = (r / 255., g / 255., b / 255.)  

    # Typically the plot is ~1.33x wider than tall.        
    # Common sizes: (10, 7.5) and (12, 9)    
    plt.figure(figsize=(12, 9))
    
    plt.plot(rc.radio, rc.velocity, 
             linewidth=2.5, color=colorpalette[0], label="bulge's rc") 
   
    # Limit the range of the plot
    plt.ylim(0, 200)    
    plt.xlim(0, 30)

    # Write text in the plot 
    plt.text(12, 70, 'text starting at (12,70)', fontsize=26)

    # Set ticks properties          
    plt.xticks(range(0, 35, 5))
    plt.tick_params(axis='both', labelsize=24) 

    # Set axis labels
    plt.ylabel("$\mathrm{ v \; [km/s]} $"); 
    plt.xlabel('R [kpc]');
    
    # Set default font family and size
    plt.rc('font', family='serif', serif='cmr10', size=32)
    
    # Set legend 
    plt.legend(frameon=False, prop={'size':20}, ncol=3, loc=2)
 
    # Set grid      
    plt.grid()  
     
    plt.show()  
    # Finally, save the figure as a PNG.    
    # You can also save it as a PDF, JPEG, etc. Just change the file extension in this call.    
    # bbox_inches="tight" removes all the extra whitespace on the edges of your plot.    
    plt.savefig('example-bulgeRC.png', bbox_inches='tight') 
    
def plot_errorbar(filename, headernames):
    """
    2D errorbar plot
    """
    # Read the data into a pandas DataFrame  
    rc = pd.read_csv(filename, # filename
                    sep='\s+', # whitespace separates the columns 
                    skiprows=[0], # skip the first row
                    header = None, # no header files to read 
                    names = headernames) # header files
   
    colorpalette = greenorange12 

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
    for i in range(len(colorpalette)):    
        r, g, b = colorpalette[i]    
        colorpalette[i] = (r / 255., g / 255., b / 255.)  

    # Typically the plot is ~1.33x wider than tall.        
    # Common sizes: (10, 7.5) and (12, 9)    
    plt.figure(figsize=(12, 9))
    
    # Two options or plotting (comment/uncomment the option you want): 
    # -) either use errorbars 
    #plt.errorbar(rc.radio, rc.velocity, yerr=rc.sigmavelocity, 
    #         fmt='+', color=colorpalette[0], label="bulge's rc")
    # -) or use matplotlib's fill_between() call to create error bars         
    plt.fill_between(rc.radio, rc.velocity - rc.sigmavelocity,  
                 rc.velocity + rc.sigmavelocity, color=colorpalette[0])
    plt.plot(rc.radio, rc.velocity, color=colorpalette[3], lw=2)
                 
    # Limit the range of the plot
    plt.ylim(0, 200)    
    plt.xlim(0, 30)

    # Write text in the plot 
    plt.text(12, 70, 'text starting at (12,70)', fontsize=26)

    # Set ticks properties          
    plt.xticks(range(0, 35, 5))
    plt.tick_params(axis='both', labelsize=24) 

    # Set axis labels
    plt.ylabel("$\mathrm{ v \; [km/s]} $"); 
    plt.xlabel('R [kpc]');
    
    # Set default font family and size
    plt.rc('font', family='serif', serif='cmr10', size=32)
    
    # Set legend 
    plt.legend(frameon=False, prop={'size':20}, ncol=3, loc=2)
 
    # Set grid      
    plt.grid()  
     
    plt.show()  
    # Finally, save the figure as a PNG.    
    # You can also save it as a PDF, JPEG, etc. Just change the file extension in this call.    
    # bbox_inches="tight" removes all the extra whitespace on the edges of your plot.    
    plt.savefig('example-bulgeRC.png', bbox_inches='tight') 
 
    
          
filename = '/Users/maria/GitHub/astro-ictp-sp/example/BGbulge_rcI.dat'
columns = ['velocity', 'sigmavelocity', 'radio']

#plot_xy(filename, columns)
plot_errorbar(filename, columns)