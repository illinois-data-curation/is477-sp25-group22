import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("results", exist_ok=True)

divvydf = pd.read_csv("data/cleaned_2024_divvy_data.csv")
weatherdf = pd.read_json("data/weather_2024.json")

#Question 1: When are Divvy bikes most frequently used in terms of time of day, day of the week, and season?

# Convert to datetime format 
divvydf['start_time'] = pd.to_datetime(divvydf['start_time'], format="%H:%M:%S", errors="coerce")
divvydf['start_date'] = pd.to_datetime(divvydf['start_date'])

# Extract time-related features
divvydf['hour'] = divvydf['start_time'].dt.hour
divvydf['weekday'] = divvydf['start_date'].dt.day_name()
divvydf['month'] = divvydf['start_date'].dt.month_name()

# Prepare data for plots
hourly_usage = divvydf['hour'].value_counts().sort_index()
weekday_usage = divvydf['weekday'].value_counts().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
monthly_usage = divvydf['month'].value_counts().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]).dropna()

# Plotting
# Plot 1: Divvy Rides by Hour of Day
plt.figure(figsize=(8, 6))
hourly_usage.plot(kind='bar', color='skyblue')
plt.title("Divvy Rides by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Rides")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("results/Divvy_Hours.png")


# Plot 2: Divvy Rides by Day of Week
plt.figure(figsize=(8, 6))
weekday_usage.plot(kind='bar', color='lightgreen')
plt.title("Divvy Rides by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Number of Rides")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("results/Divvy_Days.png")

# Plot 3: Divvy Rides by Month
plt.figure(figsize=(8, 6))
monthly_usage.plot(kind='bar', color='salmon')
plt.title("Divvy Rides by Month (Seasonal Trends)")
plt.xlabel("Month")
plt.ylabel("Number of Rides")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("results/Divvy_Months.png")

# Question 2: How does temperature impact Divvy rides?

#Displays the daily trips made on each date
daily_trips = divvydf.groupby("start_date").size().reset_index(name="trip_count")

weatherdf["DATE"] = pd.to_datetime(weatherdf["DATE"])
weatherdf["start_date"] = weatherdf["DATE"]
weatherdf.drop(columns="DATE", inplace=True, errors="ignore")

# Merge datasets on date
merged_df = pd.merge(daily_trips, weatherdf, on = "start_date")


#TAVG vs trip_count
plt.figure(figsize=(10, 6))
plt.scatter(merged_df["TAVG"], merged_df["trip_count"], alpha=0.6, color="teal")
plt.title("Effect of Average Temperature on Divvy Bike Usage")
plt.xlabel("Average Temperature (°F)")
plt.ylabel("Number of Bike Trips")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Divvy_temp.png")

# Question 3: How do weather conditions, such as Snow and precipitation, impact the daily volume of Divvy bike rides?

#Trip count during Precipitation & Snowfall
plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
sns.scatterplot(data=merged_df, x="trip_count", y="PRCP")
plt.title("Effect of Bike Trips on Precipitation")
plt.xlabel("Trip Count")
plt.ylabel("Precipitation (inches)")
plt.grid(True)

plt.subplot(1, 2, 2)
sns.scatterplot(data=merged_df, x="trip_count", y="SNOW")
plt.title("Effect of Bike Trips on Snowfall")
plt.xlabel("Trip Count")
plt.ylabel("Snowfall (inches)")
plt.grid(True)

plt.tight_layout()
plt.savefig("results/Divvy_precip.png")

#Trip Count vs Precipitation (only on days it rained/snowed)
updatedprecip_df = merged_df[(merged_df["PRCP"] > 0.0)]
updatedsnow_df = merged_df[(merged_df["SNOW"] > 0)]


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(data=updatedprecip_df, x="trip_count", y="PRCP")
plt.title("Effect of Bike Trips on Precipitation (PRCP > 0)")
plt.xlabel("Trip Count")
plt.ylabel("Precipitation (inches)")
plt.grid(True)


plt.subplot(1, 2, 2)
sns.scatterplot(data=updatedsnow_df, x="trip_count", y="SNOW")
plt.title("Effect of Bike Trips on Snowfall (SNOW > 0)")
plt.xlabel("Trip Count")
plt.ylabel("Snowfall (inches)")
plt.grid(True)

plt.tight_layout()
plt.savefig("results/Divvy_onlyprecip.png")

