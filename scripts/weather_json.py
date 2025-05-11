import pandas as pd


csv_file = pd.read_csv("raw_data/chicago_weather.csv")

# Drop unwanted columns first
columns_to_drop = ["WT01", "WT02", "WT03", "WT04", "WT05", "WT06", "WT08", "WT09"]
csv_file.drop(columns=columns_to_drop, inplace=True, errors="ignore")

json_data = csv_file.to_json(orient="records")

with open("data/weather_2024.json", "w") as outfile:
    outfile.write(json_data)
