import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab



roman_emperors = pd.read_csv('roman-emperor-reigns.csv')
roman_emperor_reign_lengths = roman_emperors['Length_of_Reign'].values
roman_emperors = roman_emperors['Emperor'].values

print (roman_emperor_reign_lengths); 

plt.hist(roman_emperor_reign_lengths)
plt.title("Roman Emperor Histogram")
plt.xlabel("Value")
plt.ylabel("Reigning")
plt.figure()
plt.savefig('foo.png', bbox_inches='tight')
plt.show()
# pd.DataFrame.hist(roman_emperor_reign_lengths); 