# Edgar Pichardo 
# This program read a data file and plots it, as well as the average 

import matplotlib.pyplot as plt
import numpy as np 

# open the levels file, which has one depth measurement per line 
with open("levels.dat","r") as data:
	#read the data, which are strings, and
	#use the numpy library to convert to floats 
	levels = np.float64(data.readlines())

	#find average level
	avg = np.mean(levels)

	#generate a line plot of the data
	plt.plot(levels)
	#plot the average line and annnotate it 
	plt.plot([0,len(levels)],[avg,avg],"--")
	plt.annotate(f"mean={avg:.2f}m", [len(levels),avg], [0,10],
	textcoords="offset pixels",ha="right")

	#label the y axis 
	plt.ylabel("level (m)")
	
	#ensure everything fits 
	plt.tight_layout()

	#save the plot and display it 
	plt.savefig("levels.png",bbox_inches="tight")
	plt.show()
