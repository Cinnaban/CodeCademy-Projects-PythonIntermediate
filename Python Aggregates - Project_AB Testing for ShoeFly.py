'''
Question 1
Examine the first few rows of ad_clicks.

Question 2
Your manager wants to know which ad platform is getting you the most views.
How many views (i.e., rows of the table) came from each utm_source?

Question 3
If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.
Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.

Question 4
We want to know the percent of people who clicked on ads from each utm_source.
Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.

Question 5
Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.
Save your results to the variable clicks_pivot.

Question 6
Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
Was there a difference in click rates for each source?

Question 7
The column experimental_group tells us whether the user was shown Ad A or Ad B.
Were approximately the same number of people shown both adds?

Question 8
Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

Question 9
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.

Question 10
For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.

Question 11
Compare the results for A and B. What happened over the course of the week?
Do you recommend that your company use Ad A or Ad B?
'''

import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())

most_views = ad_clicks.groupby('utm_source').day.count().reset_index()
#Renames columns for aesthetic purposes
#most_views = most_views.rename(columns={'utm_source':'Source','day':'views'})
#print(most_views)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head())

click_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
#print(click_by_source)

click_pivot = click_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
#print(click_pivot)

click_pivot['percent_clicked'] = click_pivot[True]/(click_pivot[True] + click_pivot[False])
#print(click_pivot)

Ad_AB = ad_clicks.groupby('experimental_group').day.count().reset_index()
#Renames columns for aesthetic purposes
#Ad_AB = Ad_AB.rename(columns={'experimental_group':'Test Group', 'day': 'Participants'})
#print(Ad_AB)

Ad_clicked = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
#print(Ad_clicked)

Ad_pivot = Ad_clicked.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()
#print(Ad_pivot)

Ad_pivot['True_P'] = Ad_pivot[True] / (Ad_pivot[True] + Ad_pivot[False])
Ad_pivot['False_P'] = Ad_pivot[False] / (Ad_pivot[True] + Ad_pivot[False])
#print(Ad_pivot)

a_clicks = ad_clicks[
  ad_clicks.experimental_group == 'A'
]
b_clicks = ad_clicks [
  ad_clicks.experimental_group == 'B'
]
#print(a_clicks.head())
#print(b_clicks.head())

day_a_clicks = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
day_b_clicks = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
#print(day_a_clicks.head())
#print(day_b_clicks.head())

Pivot_A_Clicks = day_a_clicks.pivot(
  columns = 'is_click',
  index = 'day', 
  values = 'user_id'
).reset_index()
Pivot_B_Clicks = day_b_clicks.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
#print(Pivot_A_Clicks)
#print(Pivot_B_Clicks)

Pivot_A_Clicks['Percent Clicked'] = Pivot_A_Clicks[True] / (Pivot_A_Clicks[True] + Pivot_A_Clicks[False])
Pivot_B_Clicks['Percent Clicked'] = Pivot_B_Clicks[True] / (Pivot_B_Clicks[True] + Pivot_B_Clicks[False])
print(Pivot_A_Clicks)
print(Pivot_B_Clicks)
#Recommend Ad A, because of the higher click percentage over Ad B
