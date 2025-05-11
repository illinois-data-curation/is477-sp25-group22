import pandas as pd
import os


os.makedirs("data", exist_ok=True)

folder_path = "data"
csv_files = [
    "raw_data/202401-divvy-tripdata.csv",
    "raw_data/202402-divvy-tripdata.csv",
    "raw_data/202403-divvy-tripdata.csv",
    "raw_data/202404-divvy-tripdata.csv",
    "raw_data/202405-divvy-tripdata.csv",
    "raw_data/202406-divvy-tripdata.csv",
    "raw_data/202407-divvy-tripdata.csv",
    "raw_data/202408-divvy-tripdata.csv",
    "raw_data/202409-divvy-tripdata.csv",
    "raw_data/202410-divvy-tripdata.csv",
    "raw_data/202411-divvy-tripdata.csv",
    "raw_data/202412-divvy-tripdata.csv",
]



# Read and combine all files into a single DataFrame
combined_df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# Drop columns
columns_to_drop = [
    "start_station_name", "start_station_id",
    "end_station_name", "end_station_id",
    "start_lat", "start_lng",
    "end_lat", "end_lng",
    "member_casual"
]
combined_df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

# Proper datetime format (Splitting the Dates Provided in the data set to date & time and consistent format)
combined_df['started_at'] = combined_df['started_at'].astype(str).str.split('.').str[0]
combined_df['ended_at'] = combined_df['ended_at'].astype(str).str.split('.').str[0]


combined_df['started_at'] = pd.to_datetime(combined_df['started_at'])
combined_df['ended_at'] = pd.to_datetime(combined_df['ended_at'])

combined_df['start_date'] = combined_df['started_at'].dt.date
combined_df['start_time'] = combined_df['started_at'].dt.time
combined_df['end_date'] = combined_df['ended_at'].dt.date
combined_df['end_time'] = combined_df['ended_at'].dt.time

combined_df.drop(columns=['started_at', 'ended_at'], inplace=True)

# Save
combined_df.to_csv("data/combined_2024_divvy_data.csv", index=False)
