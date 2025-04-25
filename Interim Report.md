
# Status Report  
**Group 22 - Otae K, Gabriela E**

---

## Update on Tasks


As of now, we have completed several key milestones outlined in our project plan. The GitHub repository follows a structured folder layout under the organization, including a `raw_data/` directory that contains the acquired datasets. We have also completed the `ProjectPlan.md` file, which documents our research questions and outlines the objectives of the project.

Regarding data acquisition, we identified and obtained the Divvy daily trip data for all months in 2024. These were successfully combined into a single dataset (`combined_2024_divvy_data.csv`) using a merging script & partial formatting (`merge_divy.py`) located in the root directory of the repository. Using Pandas, we read and combined all monthly files into one DataFrame, dropping unnecessary columns, which was a missing feature from the original Divvy dataset. Finally, we cleaned the datetime columns by splitting them into separate date and time columns before saving the processed file.

We have also acquired and processed weather data from the NOAA GHCND Station at Chicago O’Hare, which provides 2024 weather data for the Chicago area. This data is included in `raw_data/chicago_weather.csv`. Using a JSON converter script (`weather_json.py`), we converted the CSV file into JSON format and removed some unnecessary columns, resulting in the file `weather_2024.json` located in the root directory of the repository.

Following this, we performed data profiling, quality assessment, and initial integrity checks using hashing within the file (`assessment.ipynb`). From these preliminary checks, while the weather data (`weather_2024.json`) appeared fairly clean and consistent, we found some duplicates in the `combined_2024_divvy_data.csv` file. Within the same Python notebook, we applied a cleaning script to remove those duplicates and created a new dataset, `cleaned_2024_divvy_data.csv`. We also conducted additional integrity checks using hashing to detect any unexpected changes in both datasets.

Continuing from this, we performed an initial exploratory data analysis, documented in the Jupyter notebook `final_project.ipynb`. This includes workflow visualizations and scatter plots examining relationships between trip counts, temperature, snowfall, and precipitation. In this phase of the project, we integrated multiple steps by conducting exploratory data analysis and creating visualizations of trip trends in relation to weather conditions, which provided several insights addressing the majority of our research questions. Additionally, we documented data transformation steps with written comments in the code and markdown cells to explain our cleaning decisions.

Finally, to support reproducibility, we have initiated this process by adding a `requirements.txt` and `Environment.md` file. This ensures that future users who wish to reproduce the project can easily install all the necessary packages and Python version to proceed. The project plan and timeline are outlined in `ProjectPlan.md`, and we are currently iterating on insights and enhancing visualizations for the interim report. We have also made some adjustments to our project plan, which will be discussed further below.

---

## Weather JSON Columns

| Column | Description |
|--------|-------------|
| STATION | Unique NOAA station identifier |
| NAME | Full name and location of the weather station |
| LATITUDE | Latitude of Weather Station Location |
| LONGITUDE | Longitude of Weather Station Location |
| ELEVATION | Elevation of the station above sea level (in meters) |
| DATE | Observation date in YYYY-MM-DD format |
| PRCP | Daily precipitation (in inches) |
| SNOW | Daily snowfall (in inches) |
| SNWD | Snow depth at the time of observation (in inches) |
| TAVG | Average daily temperature (in degrees Fahrenheit) |
| TMAX | Maximum daily temperature (in degrees Fahrenheit) |
| TMIN | Minimum daily temperature (in degrees Fahrenheit) |

---

## Cleaned_2024_divvy_data.csv Columns

| Column | Description |
|--------|-------------|
| ride_id | Unique identifier for each individual ride |
| rideable_type | Type of bike used (e.g., classic, electric) |
| start_date | Date when the ride began (YYYY-MM-DD format) |
| start_time | Time when the ride began (HH:MM:SS format) |
| end_date | Date when the ride ended (YYYY-MM-DD format) |
| end_time | Time when the ride ended (HH:MM:SS format) |

---

## Updated Timeline

| Week | Task | Team Member Responsible |
|------|------|--------------------------|
| 8 | Create GitHub repository under the organization; set up project folder structure and environment | Both |
| 9 | Define and document research questions in ProjectPlan.md; explain project motivation and objectives | Both |
| 10 | Identify and acquire datasets: Divvy trip data (CSV) and Chicago weather data (JSON) | Otae |
| 10 | Evaluate dataset licenses; trace original sources and document licensing approach in Markdown | Otae |
| 11 | Perform data profiling, quality assessment (missingness, duplicates, data types); run initial integrity checks (e.g., hashes) | Otae |
| 11 | Clean, standardize, and merge datasets (e.g., unify datetime formats, align by date/station) | Otae |
| 12 | Conduct exploratory data analysis (EDA); identify patterns by time, location, and user type | Gabriela |
| 12 | Document data transformations, assessment, and cleaning decisions using Markdown and Jupyter notebooks | Both |
| 13 | Create visualizations of trip trends (hour, weekday, season), user comparisons | Gabriela |
| 13 | Begin building a reproducible Python package | Both |
| 13 | Write Status (Interim Report) | Both |
| 14 | Automate end-to-end data workflow (acquisition, cleaning, merging, EDA, visualization) using scripts | Otae |
| 14 | Finish and validate reproducibility of workflow across environments (Jupyter, CLI) | Both |
| 15 | Write up final findings in Markdown; update project documentation with accurate citations of data and software | Gabriela |
| 15 | Create Metadata describing your package, and archive project in repository obtaining a persistent identifier | Both |

---

## Changes Made on the Project

One of our original research questions aimed to explore geographic patterns in bike usage across different neighborhoods or stations in Chicago. However, we were unable to pursue this due to a lack of detailed location-based data. The available weather information from NOAA only provided general insights for the greater Chicago area, without station-specific or neighborhood-level granularity. As a result, we revised our research focus to a more feasible question: **“How does temperature in Chicago affect Divvy bike usage?”** This allowed us to analyze the relationship between temperature and ride frequency, which we visualized and documented in `final_project.ipynb` to highlight relevant trends and correlations.

Another change we made was shifting our focus from the 2025 Divvy data to the 2024 dataset. This decision allowed us to access a more complete set of data with additional months available, enabling a more thorough analysis of seasonal trends in bike usage. With more data to work with, we were able to draw stronger connections between weather conditions and ride patterns, create more meaningful visualizations, and better understand how Divvy bike usage fluctuated throughout the year.

We have also included instructions on how to access the data for both raw datasets in the updated `ProjectPlan.md`.

---

## Future Steps

In the next few weeks, we will focus on making our reproducible package ready so that other individuals can simply replicate our findings and analysis easily. This is done by making our scripts, data, and documentation readable. We will also set up an end-to-end automated process that addresses data acquisition, cleaning, merging, and visualization to simplify the entire process. As part of our commitment to transparency and intellectual honesty, we will also offer exact citations for every dataset and software tool that we use. We will also create full metadata to describe the structure and workings of our package. Finally, we will commit the whole project to a repository and obtain an enduring identifier in order to ensure long-term accessibility and reproducibility.
