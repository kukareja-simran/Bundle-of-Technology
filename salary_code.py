#!/usr/bin/python3
import joblib 
regressor = joblib.load('salary.pk1')
i = input("Enter experience: ")
a = regressor.predict([[int(i)]])
print("The predicted salary of a person with {} years experience is {}".format(i,a))





