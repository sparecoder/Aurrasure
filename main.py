import pandas as pd 
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

data= pd.read_csv('C:/Users/KIIT/Downloads/Timehacks_synchronize2')
print(data.shape)
# print(data.describe)
#Define the values to be considered as invalid
invalid_values = ["Null", "N/A", 0]

# Convert constant values for more than 5 mins to invalid
for column in data.columns:
    if data[column].nunique() == 1 and data[column].count() >5* 60:  #Assuming data is in seconds
        invalid_values.append(data[column].iloc[0])

# Replace invalid values with NaN
data.replace(invalid_values, pd.NA, inplace=True)

#Drop rows with invalid values
data.dropna(inplace=True)

# Optionally, reset index if you want
# data.reset_index(drop=True, inplace=True)

# Save the cleaned dataset
# clean_data= "C:/Users/KIIT/Desktop/aurrasure/cleaned_dataset2.csv"
# data.to_csv('C:/Users/KIIT/Desktop/aurrasure/cleaned_dataset2.csv', index=False)
# clean_data= pd.read_csv('C:/Users/KIIT/Desktop/aurrasure/cleaned_dataset2.csv')
output_path= "C:/Users/KIIT/Desktop/aurrasure/cleaned_dataset.csv"
data.to_csv(output_path, index=True)
clean_data= pd.read_csv(output_path)
# print(clean_data.isnull().sum())
print(clean_data.shape)

# print(clean_data['pm10'].value_counts())
# print(clean_data[ 'pm2_5'].value_counts())
X= clean_data.drop(columns='pm10'+'pm2_5'+'humidity'+'temperature',axis=1)
