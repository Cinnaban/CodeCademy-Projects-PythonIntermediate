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