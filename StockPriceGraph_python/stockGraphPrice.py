#Author: Albert Zhong 7-8-2019
# Stock Price Graph

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df = pd.read_csv("GE.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_') #removes the spaces from the column names


fig = plt.figure()

#creating two plots with different x-axis intervals. 
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

#adjust depending on the number of datapoints np.arange(min, max, interval)
major_ticks = np.arange(0, 251, 20) 
minor_ticks = np.arange(0, 251, 10)



ax1.plot(df.date, df.adj_close, 'g') #top plot, date and adj_close from excel file
ax1.grid(which='both') #enables both x and y axis grids

ax2.plot(df.date, df.adj_close) #bottom plot
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)
ax2.grid(which='both')
ax2.grid(which='minor', alpha=0.2) #??
ax2.grid(which='major', alpha=0.5) #??


#labels
#plt.xlabel('Date')
#plt.ylabel('Adj Close ($)')

#ax1.set_xlabel('Date')
ax1.set_ylabel('Adj Close ($)')
ax2.set_xlabel('Date')
ax2.set_ylabel('Adj Close ($)')
plt.xticks(fontsize=8)

plt.show()



