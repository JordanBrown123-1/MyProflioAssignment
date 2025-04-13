import statistics
import numpy as np
import matplotlib.pyplot as plt
import random
import math

dates = [f'Day {i+1}' for i in range(14)]
temperatures = [random.uniform(15, 30) for _ in range(14)]  # Temperatures in °C

#Calculate the min, max, mean, and standard deviation of the temperatures

min_temperature = round(min(temperatures),2)
print(f"Minimum temperature: {min_temperature}°C")

max_temperature = round(max(temperatures),2)
print(f"Maximum temperature: {max_temperature}°C")

mean_temperature = round(statistics.mean(temperatures),2)
print(f"Mean temperature: {mean_temperature}°C")

std_deviation = round(statistics.stdev(temperatures),2)
print(f"Standard deviation: {std_deviation}°C")

#Identify any anomalies in the temperatures with their temperature

anomalies = []
for i, temperature in enumerate(temperatures):
  if temperature < min_temperature or temperature > max_temperature:
     anomalies.append(f'Day {i+1}: {temperature}°C')
if anomalies:
  print("Anomalies:")
  for anomaly in anomalies:
    print(anomaly)
else:
  print("No anomalies detected.")

#print line chart
plt.plot(dates, temperatures, marker='o')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Data')
plt.show()

#The temperatures are evenly distributed

      
  
