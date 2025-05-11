rule reproduce_all:
    input:
        "data/combined_2024_divvy_data.csv",
        "data/cleaned_2024_divvy_data.csv",
        "data/weather_2024.json",
        "results/Divvy_Hours.png",
        "results/Divvy_Days.png",
        "results/Divvy_Months.png",
        "results/Divvy_temp.png",
        "results/Divvy_precip.png",
        "results/Divvy_onlyprecip.png"

rule combine_divvy_data:
    input:
        [
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
            "raw_data/202412-divvy-tripdata.csv"
        ]
    output:
        "data/combined_2024_divvy_data.csv"
    shell:
        "python3 scripts/merge_divy.py"

rule convert_weather_data:
    input:
        "raw_data/chicago_weather.csv"
    output:
        "data/weather_2024.json"
    shell:
        "python3 scripts/weather_json.py"

rule cleaning_data:
    input:
        divvy="data/combined_2024_divvy_data.csv",
        weather="data/weather_2024.json"
    output:
        "data/cleaned_2024_divvy_data.csv"
    shell:
        "python3 scripts/assessment.py"

rule visualizations:
    input:
        "data/cleaned_2024_divvy_data.csv",
        "data/weather_2024.json"
    output:
        "results/Divvy_Hours.png",
        "results/Divvy_Days.png",
        "results/Divvy_Months.png",
        "results/Divvy_temp.png",
        "results/Divvy_precip.png",
        "results/Divvy_onlyprecip.png"
    shell:
        "python3 scripts/visualization.py"


