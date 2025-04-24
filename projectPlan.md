
# Project Plan
**Group 22 - Otae K, Gabriela E**

## Overview
This project investigates trends in public bike share usage in Chicago, focusing on the Divvy system data. By analyzing temporal, geographic, and environmental patterns, the study aims to identify key insights into when and where bike share services are most utilized. Additionally, it examines the impact of external factors, such as weather conditions, on user behavior.

The insights gained from this analysis can benefit city planners, policymakers, and businesses seeking to optimize bike share infrastructure and improve sustainable urban mobility. The project leverages datasets from Divvy bike share trip logs and historical weather data to answer critical research questions. Using data engineering, analysis, and visualization techniques, we aim to uncover patterns that can help improve transportation planning and accessibility in Chicago.

## Research Question(s)
- When are Divvy bikes most frequently used in terms of time of day, day of the week, and season?
- Are there any notable geographic patterns in bike usage across different neighborhoods or stations in Chicago?
- How do weather conditions, such as temperature and precipitation, impact the daily volume of Divvy bike rides?

## Team

### Otae Kwon – Data Engineer
- Responsible for acquiring and cleaning the datasets, ensuring they are structured appropriately for analysis.
- Implements data integrity checks, including verifying dataset completeness and accuracy.
- Merges the Divvy bike trip data with weather datasets to enable cross-analysis.
- Develops Python scripts to automate the dataset acquisition and preprocessing pipeline.

### Gabriela Espinosa – Data Analyst & Visualization Specialist
- Conducts exploratory data analysis (EDA) to uncover patterns and trends in the data.
- Creates meaningful visualizations to illustrate key findings.
- Analyzes the relationship between weather conditions and bike usage patterns.
- Documents findings and ensures insights are communicated effectively in the final report.

## Datasets

### 1. 2024 Divvy Bike Share Data
- **Description**: This dataset contains historical trip records from Chicago's Divvy bike share system. It includes timestamps, station locations, trip durations, and user types.
- **Format**: CSV
- **Source**: [Divvy data](https://divvy-tripdata.s3.amazonaws.com/index.html)
- **Update Frequency**: Monthly
- **Access Method**: Downloadable CSV files
- **License**: Creative Commons Attribution 4.0 (CC BY 4.0)
- **Access:** Download all datasets starting with `2024##-divvy-tripdata.zip`, continuing sequentially until the number reaches 12, and place the data into the `raw_data` folder.

### 2. Weather Data
- **Description**: This dataset includes historical weather information for Chicago, including temperature, precipitation, wind speed, and humidity.
- **Format**: JSON
- **Source**: [NOAA GHCND Station USW00094846 – Chicago O'Hare](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094846/detail)
- **Update Frequency**: Daily
- **Access Method**: Direct Download
- **License**: NOAA data is public domain, but attribution is recommended.
- **Access**: Instructions for Downloading GHCN-Daily Data:

    1. **Visit the Website**  
   Navigate to the website where GHCN-Daily data is available.

    2. **Add Data to Cart**  
   Click on **Add to Cart** for the desired dataset.

    3. **Select Output Format**  
   Choose **Custom GHCN-Daily CSV** as the output format.

    4. **Specify Data Range**  
   Set the date range to:  
   `2024-01-01` to `2024-12-31`

    5. **Configure Station Details & Data Flags**  
   - **Station Name**  
   - **Geographic Location**

    6. **Select Data Types for Custom Output**  
   - **Precipitation**  
   - **Air Temperature**

   7. **Download Data and Rename to `chicago_weather.csv` and put it into `raw_data` folder**


## Timeline

| **Week** | **Task**                                                                                                                             | **Team Member Responsible** |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| 8        | Create GitHub repository under the organization; set up project folder structure and environment                                     | Both                         |
| 9        | Define and document research questions in ProjectPlan.md; explain project motivation and objectives                                  | Both                         |
| 10       | Identify and acquire datasets: Divvy trip data (CSV) and Chicago weather data (via API)                                              | Otae                         |
| 10       | Evaluate dataset licenses; trace original sources and document licensing approach in Markdown                                        | Otae                         |
| 10       | Implement data acquisition scripts (API call for weather, direct download for Divvy); log metadata                                   | Otae                         |
| 11       | Perform data profiling, quality assessment (missingness, duplicates, data types); run initial integrity checks (e.g., hashes)       | Otae                         |
| 11       | Clean, standardize, and merge datasets (e.g., unify datetime formats, align by date/station)                                         | Otae                         |
| 12       | Conduct exploratory data analysis (EDA); identify patterns by time, location, and user type                                          | Gabriela                     |
| 12       | Document data transformations, assessment, and cleaning decisions using Markdown and Jupyter notebooks                               | Both                         |
| 13       | Create visualizations of trip trends (hour, weekday, season), user comparisons, and map popular stations                             | Gabriela                     |
| 13       | Begin building reproducible Python package                                                                                           | Both                         |
| 13       | Write Status (Interim Report)                                                                                                        | Both                         |
| 14       | Automate end-to-end data workflow (acquisition, cleaning, merging, EDA, visualization) using scripts                                | Otae                         |
| 14       | Test and validate reproducibility of workflow across environments (Jupyter, CLI)                                                     | Both                         |
| 15       | Write up final findings in Markdown; update project documentation with accurate citations of data and software                       | Gabriela                     |
| 15       | Create Metadata describing your package, and archive project in repository obtaining a persistent identifier                         | Both                         |
