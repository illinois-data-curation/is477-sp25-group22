import pandas as pd
import hashlib
import pandas
import os

os.makedirs("hashes", exist_ok=True)

divvydf = pd.read_csv("data/combined_2024_divvy_data.csv")
weatherdf = pd.read_json("data/weather_2024.json")

#Weather attributes
weather_summary_stats = weatherdf.describe()
weather_missing_values = weatherdf.isnull().sum()
weather_duplicates = weatherdf.duplicated().sum()
weather_unique_counts = weatherdf.nunique()
weather_data_types = weatherdf.dtypes

#Weather Summary Stats
print(weather_summary_stats)

#Weather Missing Value
print(weather_missing_values)

#Weather Duplicates
print("Weather Duplicates:" , weather_duplicates)

#Weather Unique Counts
print(weather_unique_counts)

#Weather Data Types
print(weather_data_types)

# -----------------------------------------------

#Divvy Attributes
div_summary_stats = divvydf.describe()
div_missing_values = divvydf.isnull().sum()
div_duplicates = divvydf.duplicated().sum()
div_unique_counts = divvydf.nunique()
div_data_types = divvydf.dtypes

#Basic Summary Statistics
print(div_summary_stats)

#Missing Values
print(div_missing_values)

#Duplicates
print("Divvy Duplicates:" , div_duplicates)

#Unique counts within each column
print(div_unique_counts)

#Unique data types
print(div_data_types)

# -----------------------------------------------

# Combined 2024 Divvy Data Cleaning
divvydf = divvydf.drop_duplicates()

divvydf.to_csv("data/cleaned_2024_divvy_data.csv", index=False)

cleaned_divvydf = pd.read_csv("data/cleaned_2024_divvy_data.csv")

c_div_duplicates = cleaned_divvydf.duplicated().sum()

print("Clean Duplicate Check:" , c_div_duplicates)

# -----------------------------------------------

# Integrity Checks (Hashing - Detect unexpected changes)
with open("data/cleaned_2024_divvy_data.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("hashes/divvy.sha", "w") as f:
    f.write(sha256hash)

with open("data/weather_2024.json", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("hashes/weather.sha", "w") as f:
    f.write(sha256hash)
