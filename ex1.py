#List Impletion:-
List = [1, 2, 3, 2.3, 4]
print(List)

#Tuple Impletion
Tuple = (‘Pooja’, 'For')
print("\nTuple with the use of String: ") print(Tuple)

#String Impletion
String = "Python Basic Programming " print("Creating String: ") print(String)
print("\nFirst character of String is: ") print(String[0])
print("\nLast character of String is: ") print(String[-1])

#Dictionary Impletion
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} print("Creating Dictionary: ") print(Dict)
print("Accessing a element using key:") print(Dict['Name'])
print("Accessing a element using get:") print(Dict.get(1))
myDict = {x: x**2 for x in [1,2,3,4,5]} print(myDict)
 
# Lambda Function
str1 = 'Good Morning'
rev_upper = lambda string: string.upper()[::-1] print(rev_upper(str1))

#Python Classes and Object class Bike:
name = "" gear = 0
bike1 = Bike() bike1.gear = 11
bike1.name = "Mountain Bike"
print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

#Numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5]) print(arr)
print(type(arr))

#Panda
import pandas as pd
df = pd.read_csv('data.csv') print(df.to_string())

#Mathplot Lib import sys
import matplotlib matplotlib.use('Agg')
import matplotlib.pyplot as plt import numpy as np
xpoints = np.array([0, 6]) ypoints = np.array([0, 250]) plt.plot(xpoints, ypoints) plt.show() plt.savefig(sys.stdout.buffer) sys.stdout.flush()
