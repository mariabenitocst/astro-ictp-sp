#-------------------------------------------------------------------------------
# Need the following Python libraries installed to run this code:
#    -) matplotlib
#    -) pandas
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas  as pd  # contains data structure and data analysis tools

#-------------------------------------------------------------------------------
# Using tableau data colors: 
# http://tableaufriction.blogspot.com.br/2012/11/finally-you-can-use-tableau-data-colors.html      

# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)] 


# These are the "Color Blind 10" colors as RGB.
colorblind10 = [(0, 107, 164), (255, 128, 14), (171, 171, 171), (89, 89, 89),
                (95, 158, 209), (200, 82, 0), (137, 137, 137), (162, 200, 236),
                (255, 188, 121), (207, 207, 207)]


# These are the "Green Orange 12" colors as RGB.
greenorange12 = [(50, 162, 81), (172, 217, 141), (255, 127, 15), (255, 185, 119), 
                (60, 183, 204), (152, 217, 228), (184, 90, 13), (255, 217, 74), 
                (57, 115, 124), (134, 180, 169), (130, 133, 59), (204, 201, 77)] 
                
#-------------------------------------------------------------------------------

filename = '/Users/maria/Desktop/RESULTS FROM CLUSTER/R8/BULGE/I/BGbulge_rcI.dat'
headernames = ['y', 'sigmay', 'x']

def plot_xy(filename, headernames):
    """
    2D plot
    """
    # Read the data into a pandas DataFrame  
    df = pd.read_csv(filename, # filename
                    sep='\s+', # whitespace separates the columns 
                    skiprows=[0], # skip the first row
                    header = None, # no header files to read 
                    names = headernames) # header files
   
    # We can call a column in df by two different forms. For example, to call
    # the first column:
    # -) df[[1]].values   or
    # -) df.y
    colorpalette = colorblind10 

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
    for i in range(len(colorpalette)):    
        r, g, b = colorpalette[i]    
        colorpalette[i] = (r / 255., g / 255., b / 255.)  

    # Typically the plot is ~1.33x wider than tall.        
    # Common sizes: (10, 7.5) and (12, 9)    
    plt.figure(figsize=(12, 9))
    
    plt.plot(df[[2]].values, df[[0]].values, 
             linewidth=2.5, color=colorpalette[0], label="x, y plot") 
   
    # Limit the range of the plot
    plt.ylim(0, 200)    
    plt.xlim(0, 30)

    # Write text in the plot 
    plt.text(12, 70, 'text starting at (12,70)', fontsize=26)

    # Set ticks properties          
    plt.xticks(range(0, 35, 5))
    plt.tick_params(axis='both', labelsize=24) 

    # Set axis labels
    plt.ylabel('y [units]'); 
    plt.xlabel('x [units]');
    
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
    plt.savefig('prueba.png', bbox_inches='tight') 
    
def plot_errorbar(filename, headernames):
    """
    2D errorbar plot - two forms 
    """
    # Read the data into a pandas DataFrame  
    df = pd.read_csv(filename, # filename
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
#    plt.errorbar(df[[2]].values, df[[0]].values, yerr=df[[1]].values, 
#                 fmt='+', color=colorpalette[0], label="error bar")
    # -) or use matplotlib's fill_between() call to create error bars 
    plt.fill_between(df.x, df.y - df.sigmay,  
                 df.y + df.sigmay, color=colorpalette[0])
    plt.plot(df[[2]].values, df[[0]].values, color=colorpalette[3], lw=2)
                 
    # Limit the range of the plot
    plt.ylim(0, 200)    
    plt.xlim(0, 30)

    # Write text in the plot 
    plt.text(12, 70, 'text starting at (12,70)', fontsize=26)

    # Set ticks properties          
    plt.xticks(range(0, 35, 5))
    plt.tick_params(axis='both', labelsize=24) 

    # Set axis labels
    plt.ylabel('y [units]'); 
    plt.xlabel('x [units]');
    
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
    plt.savefig('prueba.png', bbox_inches='tight') 