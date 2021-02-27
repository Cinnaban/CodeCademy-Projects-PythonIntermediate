'''
Question 1
Use Matplotlib to create a flights histogram.

Question 2
If you haven’t done so already, set the range of your histogram to (0, 365)

Question 3
Set the number of bins in your plot to 365, so you have a separate bin for each day of the year.

Question 4
Add an x-label, y-label, and title to your figure.

Question 5
Now, we’re going to set up our figure so it displays two plots at once. Above your plt.hist() line, add the following:
  plt.figure(1)
  plt.subplot(211)

Question 6
Between the last line for plotting your histogram and the show command, add plt.subplot(212).

Question 7
Under plt.subplot(212), use plt.hist() to make a histogram that displays the number of flowers that begin to bloom each day of the year.

Question 8
Label the y-axis of the plot. In the hint, we’ve added our code.

Right before calling plt.show() call plt.tight_layout(). This will prevent the labels from overlapping with the graphs.

Question 9
How would you use these histograms to help inform customers when they should go to Acadia, Maine. For example, if someone said they wanted to visit Acadia while there weren’t many people there, but while flowers were blooming, when would you recommend?

Check the hint to see how we answered this question.
'''

# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)

plt.hist(flights, range=(0, 365), bins = 365, edgecolor='black')
plt.title("Flights by Day")
plt.xlabel("Days")
plt.ylabel("Total Flights")

plt.subplot(212)
plt.hist(in_bloom, range=(0, 365), bins = 365, edgecolor='black')
plt.title("Flowers in bloom")
plt.xlabel("Days")
plt.ylabel("Flowers blooming")
plt.tight_layout()

plt.show()











