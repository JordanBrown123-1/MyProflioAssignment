import statistics
import numpy as np
import matplotlib.pyplot as plt
import random
import math

steps = [random.randint(4000, 15000) for _ in range(30)]

total_steps = sum(steps)
print(f"Total steps: {total_steps}")

mean_steps = total_steps / len(steps)
print(f"Mean steps: {mean_steps}")

max_steppers = max(steps)
print(f"Max steps: {max_steppers}")

min_steppers = min(steps)
print(f"Min steps: {min_steppers}")

#Calculates the percentages of days that at least 10,000 steps were taken
days=0
for i in range(len(steps)):
  if steps[i] >= 10000:
    days+=1
percent_days = (days/len(steps))*100
print(f"Percentage of days that at least 10,000 steps were taken: {percent_days}%")
    
    
  

#Compare average steps on weekdays versus weekends
weekdays = [step for step in steps if step >= 5000]
weekends = [step for step in steps if step < 5000]
weekdays_mean = statistics.mean(weekdays)
weekends_mean = statistics.mean(weekends)
print(f"Average steps on weekdays: {weekdays_mean}")
print(f"Average steps on weekends: {weekends_mean}")

#line chart and highlight days tha at least 10,000 steps were taken
plt.plot(steps)
plt.axhline(y=10000, color='r', linestyle='--')
plt.xlabel('Day')
plt.ylabel('Steps')
plt.title('Steps taken each day')
plt.show()

#This is a daily step tracker and it will calculate the average steps taken each day 


