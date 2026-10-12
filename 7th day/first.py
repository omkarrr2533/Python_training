import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd
import numpy as np 

days = [1,2,3,4,5]
temp = [30,32,31,35,33]

plt.plot(days, temp)
plt.title("Temperature in week")
plt.xlabel("day")
plt.ylabel("temperature")



a = [10,20,30,40,50]
b = [8,14,18,20,26]

plt.plot(days, a, color = "blue", marker="o", linestyle="--", label= "Python")
plt.plot(days, b, color = "green", marker="o", linestyle="--", label= "Java")

plt.title("weekly Scores")
plt.xlabel("day")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.show()