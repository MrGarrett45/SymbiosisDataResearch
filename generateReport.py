#! python3

import matplotlib.pyplot as plt
import openpyxl
from openpyxl.formula import Tokenizer

x_axis = [1,2,3,4] #takes values from openpyxl  
graphArr = [65, 57, 76, 13]
graphArr2 = [7, 4, 16, 0]
graphArr3 = [42, 18, 12, 1]

plt.figure(1)  #first graph
#plt.figure(figsize=(8,8))
plt.subplot(3, 1, 1)
ax = plt.gca()
ax.set_title('Patients Per Week')
ax.set_xlabel('Week #')
ax.set_ylabel('# of Patients')
plt.plot(x_axis, graphArr)

plt.subplot(3, 1, 2) #second graph
ax2 = plt.gca()
ax2.set_title('Cancellations Per Week')
ax2.set_xlabel('Week #')
ax2.set_ylabel('# of Cancellations')
plt.plot(x_axis, graphArr2)

plt.subplot(3, 1, 3) #third graph
ax3 = plt.gca()
ax3.set_title('New Patients Per Week')
ax3.set_xlabel('Week #')
ax3.set_ylabel('# of New Patients')
plt.plot(x_axis, graphArr3)

left = 0.125 #formatting values for graph
right = 0.52    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9      # the top of the subplots of the figure
wspace = 0.2   # the amount of width reserved for space between subplots,
               # expressed as a fraction of the average axis width
hspace = 0.4   # the amount of height reserved for space between subplots,


plt.text(5, 163, 'Avg. Number of Visits Before Discharge: 2.9', bbox={'facecolor':'red', 'alpha':0.5, 'pad': 10})

plt.text(5, 100, 'Some things worth noting:\nWeek 1 covers Aug 27-31, Week 2 covers Sep 5-7, Week 3 covers Sep 10-14,\nand Week 4 only covers Sep 17. Since week 4 is only looking at one day, this \nexplains why the stats suddenly drop off. For the graph of\nunique visitors for the first week I considered all patients new visitors so that \nexplains why there is such a sudden drop after that week.\n\n\nThank you for this oppurtunity and your consideration!\nGarrett McLaughlin', bbox={'facecolor':'none', 'pad':10})

plt.suptitle('Symbiosis Research Data', fontsize=14, fontweight='bold')
plt.subplots_adjust(left, bottom, right, top, wspace, hspace)
plt.show()
