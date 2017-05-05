import pandas as pd

data = pd.read_csv('bmi_and_life_expectancy.csv')

country = data[['Country']]
life_expectancy = data[['Life expectancy']]

BMI = data[['BMI']]

print(BMI)