# Edgar Pichardo 
# This program downloads this week's temperature forecast
# It also displays a plot, and saves it

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import requests 

#the user needs to supply the latitude and longitude 
if len(sys.argv) < 3:
	print("Please must supply the latitude and longitude")

#if latitude and longitude are the first two values supplied
lat,lon = float(sys.argv[1]),float(sys.argv[2])

#open meteo api url for temperature forecast at this lat/lon
url = "https://api.open-meteo.com/v1/forecast"+\
	f"?latitude={lat}&longitude={lon}&hourly=temperature_2m"


#download the data, which is javascript object notation (json)
data = requests.get(url).json()

#convert the data (in the hourly key) to a pandas dataframe 
df = pd.DataFrame.from_records(data["hourly"])
#transform the time column into a datetime format 
df.time = pd.to_datetime(df.time)
#convert temprature column to fahrenheit
df.temperature_2m = df.temperature_2m*(9/5) + 32
#save and plot the time series 
df.set_index("time",inplace=True)
df.to_excel("forecast.xlsx")
df.plot()
plt.savefig("forecast.png",bbox_inches="tight")
plt.tight_layout()
plt.show()

