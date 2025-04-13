import statistics
import numpy as np
import matplotlib.pyplot as plt

scores = [88, 76, 90, 85, 92, 67, 73, 81, 95, 78, 84, 79, 91, 87, 74, 69, 80, 82, 77, 89]

#prints mean, median, mode, and standar deviation
print("Min:", round(min(scores), 2))
print("Median:", round(statistics.median(scores), 2))
print("Max:", round(max(scores), 2))
print("Mean:", sum(scores)/len(scores))
print("Mode:", statistics.mode(scores))
print("Stanadard Deviation:", round(statistics.stdev(scores),2))

#prints histogram
plt.hist(scores, bins=10)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Histogram of Scores")
plt.show()


#prints line chart
plt.plot(scores)
plt.title("Scores")
plt.xlabel("Student")
plt.ylabel("Scores")
plt.show()

#Brief Summary
#In this exercise, we used the statistics module to calculate the mean, median, mode, and standard deviation of a list. We also used the numpy and matplotlib modules to create a histogram and line chart. The median and mean are similiar, but the mode is different. The mode is the most frequent value in a list. The histogram has a variety of different frequences, and the line chart shows the scores.