#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("data.csv")


# In[20]:


def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
array = df["Roll Number"]
n = len(df["Roll Number"])
x = int(input("\n\t\t\t\t\tEnter the Roll number of Student:"))
result = linearSearch(array, n, x)
if(result == -1):
    print("\nElement not found")
else:
    #print("\nElement found at index: ", result)
    print("\n\t\t\t\t\tName of the student:",df.iloc[result,1])
    print("\n\t\t\t\t\tRoll Number of the Student:",df.iloc[result,0])
    print("\n\t\t\t\t\tFees Paid by student:",df.iloc[result,2])

