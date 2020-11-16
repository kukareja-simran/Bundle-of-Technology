#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[9]:


df = pd.read_csv("president_county.csv")


# In[12]:


def binary_search(arr, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        return -1
  

arr = df["state"]
x = input("\n\t\t\t\t\tEnter the name of the state: ")
n = len(arr)  

result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("\n\t\t\t\t\tState Name:",df.iloc[result,0])
    print("\n\t\t\t\t\tContry Name:",df.iloc[result,1])
    print("\n\t\t\t\t\tTotal Votes:",df.iloc[result,2])
    print("\n\t\t\t\t\tPercentage:",df.iloc[result,3])
else: 
    print("\n\t\t\t\t\tElement is not present in array") 

