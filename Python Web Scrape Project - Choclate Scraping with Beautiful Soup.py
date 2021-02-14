'''
Question 1
Explore the webpage displayed in the browser. What elements could be useful to scrape here? Which elements do we not want to scrape?

Question 2
Let’s make a request to this site to get the raw HTML, which we can later turn into a BeautifulSoup object.
The URL is:
https://content.codecademy.com/courses/beautifulsoup/cacao/index.html
You can pass this into the .get() method of the requests module to get the HTML.

Question 3
Create a BeautifulSoup object called soup to traverse this HTML.
Use "html.parser" as the parser, and the content of the response you got from your request as the document.

Question 4
If you want, print out the soup object to explore the HTML.
So many table rows! You’re probably very relieved that we don’t have to scrape this information by hand.

Question 5
How many terrible chocolate bars are out there? And how many earned a perfect 5? Let’s make a histogram of this data.
The first thing to do is to put all of the ratings into a list.
Use a command on the soup object to get all of the tags that contain the ratings.

Question 6
Create an empty list called ratings to store all the ratings in.

Question 7
Loop through the ratings tags and get the text contained in each one. Add it to the ratings list.
As you do this, convert the rating to a float, so that the ratings list will be numerical. This should help with calculations later.

Question 8
Using Matplotlib, create a histogram of the ratings values:
plt.hist(ratings)
Remember to show the plot using plt.show()!
Your plot will show up at localhost in the web browser. You will have to navigate away from the cacao ratings webpage to see it.

Question 9 
We want to now find the 10 most highly rated chocolatiers. One way to do this is to make a DataFrame that has the chocolate companies in one column, and the ratings in another. Then, we can do a groupby to find the ones with the highest average rating.
First, let’s find all the tags on the webpage that contain the company names.

Question 10 
Just like we did with ratings, we now want to make an empty list to hold company names.

Question 11
Loop through the tags containing company names, and add the text from each tag to the list you just created.

Question 12
Create a DataFrame with a column “Company” corresponding to your companies list, and a column “Ratings” corresponding to your ratings list.

Question 13
Use .groupby to group your DataFrame by Company and take the average of the grouped ratings.
Then, use the .nlargest command to get the 10 highest rated chocolate companies. Print them out.
Look at the hint if you get stuck on this step!

Question 14
We want to see if the chocolate experts tend to rate chocolate bars with higher levels of cacao to be better than those with lower levels of cacao.
It looks like the cocoa percentages are in the table under the Cocoa Percent column.
Using the same methods you used in the last couple of tasks, create a list that contains all of the cocoa percentages. Store each percent as an integer, after stripping off the % character.

Question 15
Add the cocoa percentages as a column called "CocoaPercentage" in the DataFrame that has companies and ratings in it.

Question 16
Make a scatterplot of ratings (your_df.Rating) vs percentage of cocoa (your_df.CocoaPercentage).
You can do this in Matplotlib with these commands:
plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()
Call plt.clf() to clear the figure between showing your histogram and this scatterplot.
Remember that your plots will show up at the address localhost in the web browser.

Question 17
Is there any correlation here? We can use some numpy commands to draw a line of best-fit over the scatterplot.

Copy this code and paste it after you create the scatterplot, but before you call .show():
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

Question 18
We have explored a couple of the questions about chocolate that inspired us when we looked at this chocolate table.
What other kinds of questions can you answer here? Try to use a combination of BeautifulSoup and Pandas to explore some more.
For inspiration: Where are the best cocoa beans grown? Which countries produce the highest-rated bars?

'''

import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content,"html.parser")

print(soup)

ratings_tags = soup.find_all(attrs={"class": "Rating"})
ratings = []

for rating in ratings_tags[1:]:
  x = rating.get_text()
  ratings.append(float(x))

plt.hist(ratings)
plt.show()

company_name = soup.select("Company")

company = []
for name in company_name[1:]:
  company.append(name.string)

dict = {'Company': company, 'Rating': ratings} 
cr_df = pd.DataFrame.from_dict(dict)

avg_values = cr_df.groupby("Company").Rating.mean()
ten_ratings = avg_values.nlargest(10)
print(ten_ratings)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for td in cocoa_percent_tags[1:]:
  percent = int(td.get_text().strip('%'))
  cocoa_percents.append(percent)

dict["CocoaPercentage"] = cocoa_percents
plt.clf()
plt.scatter(cr_df.CocoaPercentage, cr_df.Rating)
plt.show()

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

