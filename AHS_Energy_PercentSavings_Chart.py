import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


ahs_energy_PCT = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergyPCT.csv")

ahs_energy_PCT = ahs_energy_PCT.drop([' ','Days','HS M1 Chillers (kWh)'], axis=1)                                       #This takes the data and drops the header column and the unnanmed index
ahs_energy_PCT = ahs_energy_PCT.loc[:, ~ahs_energy_PCT.columns.str.contains('^Unnamed')]                                #It then transposes the data
ahs_energy_PCT = ahs_energy_PCT.transpose()

ahs_energy_DIFF = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergyDIFF.csv")

ahs_energy_DIFF = ahs_energy_DIFF.drop([' ','Days','HS M1 Chillers (kWh)'], axis=1)                                     #This takes the data and drops the header column and the unnanmed index
ahs_energy_DIFF = ahs_energy_DIFF.loc[:, ~ahs_energy_DIFF.columns.str.contains('^Unnamed')]                                #It then transposes the data
ahs_energy_DIFF = ahs_energy_DIFF.transpose()


freq1= ahs_energy_PCT[0].tolist()                                                                                       #It creates lists from the columns of the data
x1 = [0,16,32,48,64,80]                                                                                              #Then it creates the x location for the columns

freq2= ahs_energy_PCT[1].tolist()
x2 = [2,18,34,50,66,82]

freq3= ahs_energy_PCT[2].tolist()
x3 = [4,20,36,52,68,84]

freq4= ahs_energy_PCT[3].tolist()
x4 = [6,22,38,54,70,86]

freq5= ahs_energy_PCT[4].tolist()
x5 = [8,24,40,56,72,88]

freq6= ahs_energy_PCT[5].tolist()
x6 = [10,26,42,58,74,90]

freq7= ahs_energy_PCT[6].tolist()
x7 = [12,28,44,60,76,92]



width = 2                                                                                                               # width of the bars
fig, ax = plt.subplots()
plt.style.use('grayscale')

rects1 = ax.bar(x1, freq1, width, color='blue')                                                                         # This creats the bars, with different colors and the lists
rects2 = ax.bar(x2, freq2, width, color='red')
rects3 = ax.bar(x3, freq3, width, color='green')
rects4 = ax.bar(x4, freq4, width, color='purple')
rects5 = ax.bar(x5, freq5, width, color='pink')
rects6 = ax.bar(x6, freq6, width, color='orange')
rects7 = ax.bar(x7, freq7, width, color='grey')



days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']                                   # this creates a index key

explanation = '\nThis chart shows the percent by which energy usage has decreased or increased at Andover High each day of the week since the year 2016 to 2018'

from matplotlib.ticker import FuncFormatter



ax.set_ylim(-14,41)
ax.set_xlim(-2,94)
ax.set_ylabel('Percent\n(Positive Numbers on Y-axis means savings, Negative numbers on Y-axis means more spent')        #this sets the window size
ax.set_xlabel(explanation)
ax.set_title('Average reduction over 2016\nAverage percent change of energy (kWh) per day over 2016: Electricity used by AHS between 23:00 hrs and 4:00 hrs')                                                                             #this sets the title, the xticks, the y label and the xtick labels
ax.set_xticks(x4)
ax.set_xticklabels(('HS Main (kWh)', 'LV Plug Loads (DHB)','HS DL Lighting (kWh)','HS DG Gym (kWh)','HS Kitchen Emergency (kWh)','HS CC Collins Center (kWh)'))
ax.legend(days, loc =7)                                                                                                 # it then creates the key index

formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
ax.yaxis.set_major_formatter(formatter)


def autolabel(rects,y):                           #this then annotates the bar plot
    count = 0
    for rect in rects:
        height = int(rect.get_height())              #it then reads the height of the bar and prints it above the data
        a = ahs_energy_DIFF.iat[count,y]
        count +=1

        if (a>1 or a<-1):
            a = int(a)

        if (height>0):
            ax.text(rect.get_x() + rect.get_width() / 2., 1 + height,'$' + str(a), ha='center', va='bottom')
            ax.text(rect.get_x() + rect.get_width()/2., 1*height,str(height)+'%',ha='center', va='bottom')
        elif (height<0):
            a *= -1
            ax.text(rect.get_x() + rect.get_width() / 2.,height-1, str(height) + '%', ha='center', va='bottom')
            ax.text(rect.get_x() + rect.get_width() / 2., height - 2, '-$' + str(a), ha='center', va='bottom')

autolabel(rects1, 0)                               # this calls the annotations
autolabel(rects2, 1)
autolabel(rects3, 2)
autolabel(rects4, 3)
autolabel(rects5, 4)
autolabel(rects6, 5)
autolabel(rects7, 6)

plt.axhline(y=0, xmin=-2, xmax=114, linewidth=1, color = 'k')
ax.text(6, -3, 'HS Main (kWh)', ha='center', va='bottom')
ax.text(22, 7, 'LV Plug Loads (DHB)', ha='center', va='bottom')
ax.text(38, -3, 'HS DL Lighting (kWh)', ha='center', va='bottom')
ax.text(54, -3,'HS DG Gym (kWh)', ha='center', va='bottom')
ax.text(70, 6, 'HS Kitchen Emergency (kWh)', ha='center', va='bottom')
ax.text(86, -3, 'HS CC Collins Center (kWh)', ha='center', va='bottom')

plt.show()

