'''
Question 1
All of the weather data is stored in a variable named london_data.
Print the first few rows of the dataset by calling print(london_data.head()).
Take a look at the browser to see the columns of this dataset. Here are two questions to ask yourself:
How often were measurements taken?
Which columns might be the most useful when thinking about planning a trip. 
If you want to see different rows of the data, you can try something like this:
print(london_data.iloc[100:200])
This will print rows 100 through 199.
Comment out these print statements after looking through the results.

Question 2
Let’s also take a look at how many data points we have. Print len(london_data)

Question 3
Now that we’ve seen what the data looks like, let’s dive into one of the more promising columns — "TemperatureC". This column stores the temperature in Celsius.

To get a single column from a DataFrame, you can use this syntax:

one_column = london_data["column_name"]
Create a variable named temp and set it equal to the "TemperatureC" column of london_data.

Question 4
We can now calculate descriptive statistics about this column. To begin, find the average temperature in London in 2015. Store it in a variable named average_temp.

Question 5
Calculate the variance of the temperature column and store the results in the variable temperature_var. Print the results.

Question 6
Calculate the standard deviation of the temperature column and store a variable named temperature_standard_deviation. Print this variable.

How would the variance and standard deviation help you plan a trip?

Question 7
The statistics we just calculated aren’t very helpful when trying to plan a vacation since they describe the weather throughout an entire year.

If we could find a way to use the rows from only a certain month, that might help us find the best month to plan our trip.

Once again, print london_data.head() to see the first few columns of our DataFrame. Which column will help us get only the data points from January? In the browser you can scroll to the right to see more columns.

Question 8
We want to filter by the "month" column! The following line of code will create a variable that gets the temperature from the rows where "month" is 6. These will be all of the rows from the month of June.

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
Create this variable for June.

Question 9
Create a variable named july that contains all of the data points from July. The code to do this should look very similar to your code that created the June variable. This time, we’re interested in month 7.

Question 10
Calculate and print the mean temperature in London for both June and July using the np.mean() function.

What do these numbers tell you? If you wanted to visit London on the month that was, on average, cooler, which month would you pick? Look at the hint to see our thoughts!

Question 11
Calculate and print the standard deviation of temperature in London for both June and July. Remember, the function you should use is np.std().

What do these numbers tell you? How might the standard deviation change your decision on when to visit London? Click on the hint to see our thoughts.

Question 12
If you want to quickly see the mean and standard deviation of every month, use this block of code.

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
During which month would you most like to visit? If you wanted to pick the month with the least variable temperature, which one would you pick?

'''

import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())
#print(len(london_data)) # 39106 rows of data

temp = london_data['TemperatureC']

average_temp = np.mean(temp)
temperature_var = np.var(temp)
print(temperature_var)

temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

#print(london_data.head())

june = london_data.loc[london_data['month'] == 6]
['TemperatureC']

july = london_data.loc[london_data['month'] == 7]
['TemperatureC']

print(np.mean(june))
print(np.mean(july))

print(np.std(june))
print(np.std(july))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")





