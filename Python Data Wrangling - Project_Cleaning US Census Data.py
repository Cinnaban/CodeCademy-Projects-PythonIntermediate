'''
Question 1
The first visualization your boss wants you to make is a scatterplot that shows average income in a state vs proportion of women in that state.

Open some of the census csv files in the navigator (click the file icon in the top left corner of the code editor and then click on any of the csv files to open them). How are they named? What kind of information do they hold? Will they help us make this graph?

Question 2
It will be easier to inspect this data once we have it in a DataFrame. You can’t even call .head() on these csvs! How are you supposed to read them?

Using glob, loop through the census files available and load them into DataFrames. Then, concatenate all of those DataFrames together into one DataFrame, called something like us_census.

Question 3
Look at the .columns and the .dtypes of the us_census DataFrame. Are those datatypes going to hinder you as you try to make histograms?

Question 4
Look at the .head() of the DataFrame so that you can understand why some of these dtypes are objects instead of integers or floats.

Start to make a plan for how to convert these columns into the right types for manipulation.

Question 5
Use regex to turn the Income column into a format that is ready for conversion into a numerical type.

Question 6
Look at the GenderPop column. We are going to want to separate this into two columns, the Men column, and the Women column.
Split the column into those two new columns using str.split and separating out those results.

Question 7
Convert both of the columns into numerical datatypes.
There is still an M or an F character in each entry! We should remove those before we convert.

Question 8
Now you should have the columns you need to make the graph and make sure your boss does not slam a ruler angrily on your desk because you’ve wasted your whole day cleaning your data with no results to show!

Use matplotlib to make a scatterplot!

plt.scatter(the_women_column, the_income_column) 
Remember to call plt.show() to see the graph!

Question 9
Did you get an error? These monstrous csv files probably have nan values in them! Print out your column with the number of women per state to see.

We can fill in those nans by using pandas’ .fillna() function.

You have the TotalPop per state, and you have the Men per state. As an estimate for the nan values in the Women column, you could use the TotalPop of that state minus the Men for that state.

Print out the Women column after filling the nan values to see if it worked!

Question 10
We forgot to check for duplicates! Use .duplicated() on your census DataFrame to see if we have duplicate rows in there.

Question 11
Drop those duplicates using the .drop_duplicates() function.

Question 12
Now, your boss wants you to make a bunch of histograms out of the race data that you have. Look at the .columns again to see what the race categories are.

Question 13
Now, your boss wants you to make a bunch of histograms out of the race data that you have. Look at the .columns again to see what the race categories are.

Question 14

Try to make a histogram for each one!

You will have to get the columns into numerical format, and those percentage signs will have to go.

Don’t forget to fill the nan values with something that makes sense! You probably dropped the duplicate rows when making your last graph, but it couldn’t hurt to check for duplicates again.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

us_census = []
for f in files:
  j = pd.read_csv(f)
  us_census.append(j)

census_df = pd.concat(us_census)
# What does the data look like
#print(census_df.head())
#print(len(census_df))

# What are the columns?
#print(census_df.columns)

# What are the column data types
#print(census_df.dtypes)

# Convert the income column from 'object' to 'float64'
census_df.Income = census_df['Income'].replace('[\$,]','', regex=True)

census_df.Income = pd.to_numeric(census_df.Income)
#print(census_df.head())
#print(census_df.dtypes) 

# Split the GenderPop column to Men or Women
g_split = census_df.GenderPop.str.split('_', expand=True)
census_df['Male'] = g_split[0]
census_df['Female'] = g_split[1]
#print(census_df.head())

# Remove GenderPop
census_df = census_df[['State', 'TotalPop', 'Hispanic', 'White', 'Black', 
'Native', 'Asian', 'Pacific', 'Income', 'Male', 'Female']]
#print(census_df.head())

# Remove the 'M' and 'F' from both the 'Male' and 'Female' Columns
m_split = census_df.Male.str.split('[M]', expand = True)
census_df.Male = pd.to_numeric(m_split[0])
#print(m_split.head(5))
#print(census_df.head(5))
f_split = census_df.Female.str.split('[F]', expand = True)
census_df.Female = pd.to_numeric(f_split[0])
#print(f_split.head(5))
#print(census_df.head(5))
#print(census_df.dtypes)

# Make a scatter plot
plt.scatter(census_df.Female, census_df.Income)
#plt.show()

# Number by state
ws = census_df[['Female','State']]
#print(ws)
# How many is NAN in Female
#print(census_df.Female.isna().sum())
# Populate the NAN in Female by taking Total Pop by State - Men by State
estimated_F = census_df['TotalPop']-census_df['Male']
census_df.Female = census_df.Female.fillna(estimated_F)
# Validate that there is 0 NAN 
#print(census_df.Female.isna().sum())

# How many entries are duplicates in the data frame? 
#print(census_df.duplicated().sum())
census_df = census_df.drop_duplicates()
# Validate that there is 0 duplicates
#print(census_df.duplicated().sum())

# Generate an updated Scatter plot
plt.scatter(census_df.Female, census_df.Income)
#plt.show()

# What is all the column names?
#print(census_df.columns)

# Make a histogram for each column
#print(census_df.dtypes)
#print(census_df.head(5))

# Remove % from Hispanic
H_split = census_df.Hispanic.str.split('[%]', expand = True)
census_df.Hispanic = pd.to_numeric(H_split[0])
# Remove % from White
W_split = census_df.White.str.split('[%]', expand = True)
census_df.White = pd.to_numeric(W_split[0])
# Remove % from Black
B_split = census_df.Black.str.split('[%]', expand = True)
census_df.Black = pd.to_numeric(B_split[0])
# Remove % from Native
N_split = census_df.Native.str.split('[%]', expand = True)
census_df.Native = pd.to_numeric(N_split[0])
# Remove % from Asian
A_split = census_df.Asian.str.split('[%]', expand = True)
census_df.Asian = pd.to_numeric(A_split[0])
# Remove % from Pacific
P_split = census_df.Pacific.str.split('[%]', expand = True)
census_df.Pacific = pd.to_numeric(P_split[0])
# Validate the updated columns 
#print(census_df.head())
print(census_df.dtypes)

# TotalPop by Race
plt.scatter(census_df.TotalPop, census_df.Hispanic)
plt.show()
plt.scatter(census_df.Income, census_df.White)
plt.show()
plt.scatter(census_df.Income, census_df.Black)
plt.show()
plt.scatter(census_df.Income, census_df.Native)
plt.show()
plt.scatter(census_df.Income, census_df.Asian)
plt.show()
plt.scatter(census_df.Income, census_df.Pacific)
plt.show()
plt.scatter(census_df.Income, census_df.Male)
plt.show()
plt.scatter(census_df.Income, census_df.Female)
plt.show()



