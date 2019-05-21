import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

ahs_energy_PCT = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergyPCT.csv")
ahs_energy_PCT = ahs_energy_PCT.drop([' ','Days'], axis=1)                                                              #This takes the data and drops the header column and the unnanmed index
ahs_energy_PCT = ahs_energy_PCT.loc[:, ~ahs_energy_PCT.columns.str.contains('^Unnamed')]                                #It then transposes the data
ahs_energy_PCT = ahs_energy_PCT.transpose()


freq1= ahs_energy_PCT[0].tolist()                                                                                       #It creates lists from the columns of the data
x1 = [0,10,20,30,40,50,60]                                                                                              #Then it creates the x location for the columns

freq2= ahs_energy_PCT[1].tolist()
x2 = [1,11,21,31,41,51,61]

freq3= ahs_energy_PCT[2].tolist()
x3 = [2,12,22,32,42,52,62]

freq4= ahs_energy_PCT[3].tolist()
x4 = [3,13,23,33,43,53,63]

freq5= ahs_energy_PCT[4].tolist()
x5 = [4,14,24,34,44,54,64]

freq6= ahs_energy_PCT[5].tolist()
x6 = [5,15,25,35,45,55,65]

freq7= ahs_energy_PCT[6].tolist()
x7 = [6,16,26,36,46,56,66]

freq8= [0,0,0,0,0,0,0]
x8 = [70,71,72,73,74,75,76]

width = 1                                                                                                               # width of the bars
fig, ax = plt.subplots()
plt.style.use('grayscale')

rects1 = ax.bar(x1, freq1, width, color='blue')                                                                         # This creats the bars, with different colors and the lists
rects2 = ax.bar(x2, freq2, width, color='red')
rects3 = ax.bar(x3, freq3, width, color='green')
rects4 = ax.bar(x4, freq4, width, color='purple')
rects5 = ax.bar(x5, freq5, width, color='cyan')
rects6 = ax.bar(x6, freq6, width, color='orange')
rects7 = ax.bar(x7, freq7, width, color='grey')
rects8 = ax.bar(x8, freq8, width, color='grey')


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']                                   # this creates a index key

ax.set_ylim(-20,50)
ax.set_ylabel('Percent')                                                                                                #this sets the window size
ax.set_title('Average reduction over 2016')                                                                             #this sets the title, the xticks, the y label and the xtick labels
ax.set_xticks(x4)
ax.set_xticklabels(('HS Main (kWh)', 'LV Plug Loads (DHB)','HS DL Lighting (kWh)','HS DG Gym (kWh)','HS Kitchen Emergency (kWh)','HS M1 Chillers (kWh)','HS CC Collins Center (kWh)'))
ax.legend(days, loc =7)                                                                                                 # it then creates the key index

plt.show()

