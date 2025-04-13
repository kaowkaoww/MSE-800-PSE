import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
days = ["Monday", "Tuesday", "Wednesday", "Thursday" , "Friday", "Saturday", "Sunday"]

#Average temperature
average_temparature = np.mean(temperatures)
print(f"Average Temperature : {average_temparature:.2f}", "°C")
         
#Highest and Lowest temparature
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
print("The highest temperature :", max_temp, "°C")
print("The lowest temperature :", min_temp, "°C")

#Convert celcius temp to farenheit temp
farenheit_temp = temperatures*9/5 + 32
formatted_farenheit = [f"{temperatures:.2f}" for temperatures in farenheit_temp]
print("Farenheit temperatures :", (formatted_farenheit), "°F")


#Identify the days (by index) where the temperature was above 20°C
above_20_indices = np.where(temperatures>20)[0]
above_20_days =  [days[i] for i in above_20_indices]
print("The days where the temperature was above 20°C :", above_20_days,)