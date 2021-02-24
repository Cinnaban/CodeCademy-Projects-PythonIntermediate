# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# View the first few rows of each
'''
print(brooklyn_one_bed.head())
print(manhattan_one_bed.head())
print(queens_one_bed.head())
 
print(brooklyn_price.head())
print(manhattan_price.head())
print(queens_price.head())
'''
# Add mean calculations below 
brooklyn_mean = np.mean(brooklyn_price)
#print(brooklyn_mean) #3327.40
manhattan_mean = np.mean(manhattan_price)
#print(manhattan_mean) #3993.48
queens_mean = np.mean(queens_price)
#print(queens_mean) #2346.25

# Add median calculations below
brooklyn_median = np.median(brooklyn_price)
#print(brooklyn_median) #3000
manhattan_median = np.median(manhattan_price)
#print(manhattan_median) #3800
queens_median = np.median(queens_price)
#print(queens_median) #2200

# Add mode calculations below
brooklyn_mode = stats.mode(brooklyn_price)
#print(brooklyn_mode) #ModeResult(mode=array([2500]), count=array([26]))
manhattan_mode = stats.mode(manhattan_price)
#print(manhattan_mode) #ModeResult(mode=array([3500]),count=array([56]))
queens_mode = stats.mode(queens_price)
#print(queens_mode) #ModeResult(mode=array([1750], count=array([11]))








##############################################
##############################################
##############################################






# Don't look below here
# Mean
try:
    print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
except NameError:
    print("The mean price in Brooklyn is not yet defined.")
try:
    print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
except NameError:
    print("The mean in Manhattan is not yet defined.")
try:
    print("The mean price in Queens is " + str(round(queens_mean, 2)))
except NameError:
    print("The mean price in Queens is not yet defined.")
    
    
# Median
try:
    print("The median price in Brooklyn is " + str(brooklyn_median))
except NameError:
    print("The median price in Brooklyn is not yet defined.")
try:
    print("The median price in Manhattan is " + str(manhattan_median))
except NameError:
    print("The median price in Manhattan is not yet defined.")
try:
    print("The median price in Queens is " + str(queens_median))
except NameError:
    print("The median price in Queens is not yet defined.")
    
    
#Mode
try:
    print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
except NameError:
    print("The mode price in Brooklyn is not yet defined.")
try:
    print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
except NameError:
    print("The mode price in Manhattan is not yet defined.")
try:
    print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
except NameError:
    print("The mode price in Queens is not yet defined.")


