# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:07:00 2018

@author: Sarva
"""

import pandas as pa
import matplotlib.pyplot as plt 

data= pa.read_csv('EmployeeRecord.csv')

print(type(data))

print(data)

#print(data.loc[:,'Gender'])
gender= data.loc[:,'Gender']
#print(type(gender))

gender_list=gender.tolist()

print(gender_list)
print(type(gender_list))

plt.hist(gender_list, width=0.1)
plt.ylabel('Count')
plt.ylim(400,600)
#plt.yticks(range(300,600))
plt.show()
