import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.ticker as mtick

ahs_energy_DIFF = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergyDIFF.csv")
freq = ahs_energy_DIFF['HS Main (kWh)'].tolist() #This takes the data of the price changes and makes the column that are to be plotted into lists
x = [0,2,4,6,8,10,12]                            #It then creates the x locations for where the bars should be plotted
width = 1                                        #it creates the width of the bar


fig, ax = plt.subplots()                        #This then creats the bar plot
rects1 = ax.bar(x, freq, width, color='g')      # this creates the bars

explanation = '\nThis chart shows the money saved on energy that was used at Andover High each day of the week since the year 2016 to 2018\n'


ax.set_ylim(0,20)                               #this sets the window size
ax.set_ylabel('Cost')                           #this sets the title, the xticks, the y label and the xtick labels
ax.set_xlabel(explanation)
ax.set_title('HS Main (kWh)\nAverage savings per day over 2016: Electricity used by AHS between 23:00 hrs and 4:00 hrs')
ax.set_xticks(x)
ax.set_xticklabels(('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)


def autolabel(rects):                           #this then annotates the bar plot
    for rect in rects:
        height = rect.get_height()              #it then reads the height of the bar and prints it above the data
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,'$ '+str(height)+' ',ha='center', va='bottom')

autolabel(rects1)                               # this calls the annotations
plt.show()

