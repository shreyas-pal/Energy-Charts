import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

ahs_energy_PCT = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergyPCT.csv")

ahs_energy_PCT = ahs_energy_PCT.drop([' ','Days'], axis=1)                                                              #This takes the data and drops the header column and the unnanmed index
ahs_energy_PCT = ahs_energy_PCT.loc[:, ~ahs_energy_PCT.columns.str.contains('^Unnamed')]                                #It then transposes the data
ahs_energy_PCT = ahs_energy_PCT.transpose()


freq1= ahs_energy_PCT[0].tolist()                                                                                       #It creates lists from the columns of the data
x1 = [0,16,32,48,64,80,96]                                                                                              #Then it creates the x location for the columns

freq2= ahs_energy_PCT[1].tolist()
x2 = [2,18,34,50,66,82,98]

freq3= ahs_energy_PCT[2].tolist()
x3 = [4,20,36,52,68,84,100]

freq4= ahs_energy_PCT[3].tolist()
x4 = [6,22,38,54,70,86,102]

freq5= ahs_energy_PCT[4].tolist()
x5 = [8,24,40,56,72,88,104]

freq6= ahs_energy_PCT[5].tolist()
x6 = [10,26,42,58,74,90,106]

freq7= ahs_energy_PCT[6].tolist()
x7 = [12,28,44,60,76,92,108]


width = 2                                                                                                               # width of the bars
fig, ax = plt.subplots()
plt.style.use('grayscale')

rects1 = ax.bar(x1, freq1, width, color='blue')                                                                         # This creats the bars, with different colors and the lists
rects2 = ax.bar(x2, freq2, width, color='red')
rects3 = ax.bar(x3, freq3, width, color='green')
rects4 = ax.bar(x4, freq4, width, color='purple')
rects5 = ax.bar(x5, freq5, width, color='cyan')
rects6 = ax.bar(x6, freq6, width, color='orange')
rects7 = ax.bar(x7, freq7, width, color='grey')



days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']                                   # this creates a index key

explanation = '\nThis chart shows the percent by which energy usage has decreased or increased at Andover High each day of the week since the year 2016 to 2018'

ax.set_ylim(-13,41)
ax.set_xlim(-2,114)
ax.set_ylabel('Percent')                                                                                                #this sets the window size
ax.set_xlabel(explanation)
ax.set_title('Average reduction over 2016\nAverage percent change of energy (kWh) per day over 2016: Electricity used by AHS between 23:00 hrs and 4:00 hrs')                                                                             #this sets the title, the xticks, the y label and the xtick labels
ax.set_xticks(x4)
ax.set_xticklabels(('HS Main (kWh)', 'LV Plug Loads (DHB)','HS DL Lighting (kWh)','HS DG Gym (kWh)','HS Kitchen Emergency (kWh)','HS M1 Chillers (kWh)','HS CC Collins Center (kWh)'))
ax.legend(days, loc =7)                                                                                                 # it then creates the key index


def autolabel(rects):                           #this then annotates the bar plot
    for rect in rects:
        height = int(rect.get_height())              #it then reads the height of the bar and prints it above the data
        if (height>0):
            ax.text(rect.get_x() + rect.get_width()/2., 1*height,str(height)+'%',ha='center', va='bottom')
        elif (height<0):
            ax.text(rect.get_x() + rect.get_width() / 2.,height-1, str(height) + '%', ha='center', va='bottom')

autolabel(rects1)                               # this calls the annotations
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)
autolabel(rects7)
plt.show()

