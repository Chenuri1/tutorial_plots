# Tutorial from "Matplotlib Tutorial (Part 1): Creating and Customizing Our First Plots" Series

from matplotlib import pyplot as plt 
import numpy as np

"This is will output different styles  such as solarise_light2 or  classic test patch"
#print(plt.style.available)
"This will use the type of style on your plots "
#plt.style.use('Solarize_Light2') 

dev_x = [1, 2, 3, 4]
dev_y= [1, 2 ,3, 4]
dev_y_1 = [3,6,9,12]
plt.figure(1)

plt.subplot(211)
plt.plot(dev_x,dev_y,label='First plot')
plt.legend()
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Test plot')


plt.subplot(212)                      
plt.plot(dev_x,dev_y_1, color = 'k',linestyle = '--',marker = '.',label='Second plot')

""" This way of adding a legend is error prone, because you need to know the order of the plots """
#plt.legend(['First plot','Second plot']) 
"""Alternatively you should add a label into the plt.plot plt.plot(dev_x,dev_y,label = 'First plot'). You can then just put plt.legend()"""
plt.legend()

plt.figure(2)
bar_width = 0.25
plt.bar(dev_x,dev_y,width = bar_width)
plt.figure(3)
plt.barh(dev_x,dev_y)


#saves to the current directory 
plt.savefig('first test plot.png') #saves to the current directory 


plt.show()
