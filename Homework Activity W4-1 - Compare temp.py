#Activity W4-1
#Load a data for Auckland and Christchurch and compare the temperature between two cities in a year monthly basis

import numpy as np
import pandas as pd 
import calendar


class CityTemperature:
    def __init__(self, city, file_path):
        self.city = city
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    def get_temp(self):
        return self.temp

def compare_temp(city1, city2):
    print('\n====================================================')
    print("\nThe temperature between Auckland and Christchurch in a year monthly basis\n")
    print(f"{'Year' :<8}{'Month':<15}{city1.city+' (°C)':<15}{city2.city+' (°C)':<20}Difference (°C)")

    month_names = list(calendar.month_name)[1:]

    for year in city1.data['YEAR']:
        for month_idx, month_name in enumerate(month_names, start=1):
            month_name_upper = month_name.upper()
            temp1 = city1.data.loc[city1.data['YEAR'] == year, month_name_upper].values[0]
            temp2 = city2.data.loc[city2.data['YEAR'] == year, month_name_upper].values[0]
            
            diff = round(temp1-temp2, 2)
            print(f"{year:<8}{month_name_upper:<15}{round(temp1,2):<15}{round(temp2,2):<20}{diff}")
    print('\n====================================================')

auckland = CityTemperature('Auckland', '/Users/manisa/Desktop/Firstcoding/23976__combined__Mean_air_temperature__Deg_C.csv')
christchurch = CityTemperature('Christchurch', '/Users/manisa/Desktop/Firstcoding/4858__combined__Mean_air_temperature__Deg_C.csv')

auckland.load_data()
christchurch.load_data()

compare_temp(auckland,christchurch)