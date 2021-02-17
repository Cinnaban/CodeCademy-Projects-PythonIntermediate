import pandas as pd
import csv

#pd.set_option('display.max_colwidth', None)

df = pd.read_csv('jeopardy.csv')
#print(df.head(5))
# The Column Names are: Show Number, Air Date, Round, Category, Value, Question, Answer
# Notice the column names have extra spaces 
#print(df['Show Number'].head())
#print(df[' Answer'].head())

# Rename the Columns to acquire data easier 
df = df.rename(columns={'Show Number': 'Number',' Air Date': 'Date', ' Round':'Round', ' Category':'Category', ' Value': 'Value', ' Question':'Question', ' Answer':'Answer'})
# Validate the changes 
#print(df.head(5))
#print(df['Number'].head(5))
#print(df['Date'].head(5))
#print(df['Round'].head(5))
#print(df['Category'].head(5))
#print(df['Value'].head(5))
#print(df['Question'].head(5))
#print(df['Answer'].head(5))

# Lets look for all the Questions that contain football
football_df = df[df['Question'].str.contains('football', na=False)]
#print(football_df.head())
# Now lets make a function that filters the data set for Questions that contain football

# Define the list variable
keywords = ["football","hoop"]

def my_football(keywords): 
    mask = df['Question'].apply(lambda x: any(word for word in keywords if word in x))
    return df[mask]
# Check if the function works properly & validate against the current method
#print(my_football(keywords).head())
#print(football_df.head())

# Convert the Value column into floats - current is string
df['Value_Float'] = df['Value'].apply(lambda x: x.replace('$','') if '$' in x else x)
df['Value_Float'] = df['Value_Float'].apply(lambda x: x.replace(',','') if ',' in x else x)
df['Value_Float'] = df['Value_Float'].apply(lambda x: x.replace('None','0') if 'None' in x else x)
# What is the data type of the new column? (series)
#print(type(df['Value_Float']))
# Strip any white space available
df['Value_Float'] = df['Value_Float'].str.strip()
#print(df.head(1))

# Find the average value for Keywords (pd.to_numeric converts strings to values)
df['Value_Float'] = pd.to_numeric(df['Value_Float'])
#print(df.head(1))

# Calculate the average for the 'Value Float' column (739.98)
Value_mean = df['Value_Float'].mean()
#print(Value_mean)

# Now that we have the 'Value_Float' column, what is the average value for 'Keywords'?
#print(my_football(keywords)['Value_Float'].mean())
# It works! The average value for 'Keywords' is 627.6

# Determine how many answers contain a word
word = ['K2']
def unique_word(x):
    count = len(pd.unique(df['Answer'].values == x))
    return count
#print(unique_word(word))

# Determine how many answers are unique? 88269 
def unique_answer():
    count = len(df['Answer'].unique())
    return count
print(unique_answer())

'''
1.
In order to complete this project, you should have completed the Pandas lessons in the Analyze Data with Python Skill Path. You can also find those lessons in the Data Analysis with Pandas course or the Data Scientist Career Path.

Finally, the Practical Data Cleaning course may also be helpful.

Project Requirements
2.
We’ve provided a csv file containing data about the game show Jeopardy! in a file named jeopardy.csv. Load the data into a DataFrame and investigate its contents. Try to print out specific columns.

Note that in order to make this project as “real-world” as possible, we haven’t modified the data at all — we’re giving it to you exactly how we found it. As a result, this data isn’t as “clean” as the datasets you normally find on Codecademy. More specifically, there’s something odd about the column names. After you figure out the problem with the column names, you may want to rename them to make your life easier the rest of the project.

In order to disply the full contents of a column, we’ve added this line of code to the top of your file:

pd.set_option('display.max_colwidth', -1)

Stuck? Get a hint
3.
Write a function that filters the dataset for questions that contains all of the words in a list of words. For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame of 152 rows. Every row had the strings "King" and "England" somewhere in its " Question".

Note that in this example, we found 152 rows by filtering the entire dataset. You can download the entire dataset at the start or end of this project. The dataset used on Codecademy is only a fraction of the dataset so you won’t find as many rows.

Test your function by printing out the column containing the question of each row of the dataset.


Stuck? Get a hint
4.
Test your original function with a few different sets of words to try to find some ways your function breaks. Edit your function so it is more robust.

For example, think about capitalization. We probably want to find questions that contain the word "King" or "king".

You may also want to check to make sure you don’t find rows that contain substrings of your given words. For example, our function found a question that didn’t contain the word "king", however it did contain the word "viking" — it found the "king" inside "viking". Note that this also comes with some drawbacks — you would no longer find questions that contained words like "England's".


Stuck? Get a hint
5.
We may want to eventually compute aggregate statistics, like .mean() on the " Value" column. But right now, the values in that column are strings. Convert the " Value" column to floats. If you’d like to, you can create a new column with the float values.

Now that you can filter the dataset of question, use your new column that contains the float values of each question to find the “difficulty” of certain topics. For example, what is the average value of questions that contain the word "King"?

Make sure to use the dataset that contains the float values as the dataset you use in your filtering function.


Stuck? Get a hint
6.
Write a function that returns the count of the unique answers to all of the questions in a dataset. For example, after filtering the entire dataset to only questions containing the word "King", we could then find all of the unique answers to those questions. The answer “Henry VIII” appeared 3 times and was the most common answer.


Stuck? Get a hint
7.
Explore from here! This is an incredibly rich dataset, and there are so many interesting things to discover. There are a few columns that we haven’t even started looking at yet. Here are some ideas on ways to continue working with this data:

Investigate the ways in which questions change over time by filtering by the date. How many questions from the 90s use the word "Computer" compared to questions from the 2000s?
Is there a connection between the round and the category? Are you more likely to find certain categories, like "Literature" in Single Jeopardy or Double Jeopardy?
Build a system to quiz yourself. Grab random questions, and use the input function to get a response from the user. Check to see if that response was right or wrong. Note that you can’t do this on the Codecademy platform — to do this, download the data, and write and run the code on your own computer!
Solution
8.
Compare your program to our sample solution code - remember, that your program might look different from ours (and probably will) and that’s okay!

Solution
9.
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.
'''






