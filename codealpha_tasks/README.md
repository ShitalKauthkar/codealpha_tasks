# CodeAlpha Task 2 – Exploratory Data Analysis on Netflix

## 📌 Project Overview

This project is completed as part of the **CodeAlpha Data Analytics Internship – Task 2: Exploratory Data Analysis (EDA)**.

The objective of this project is to explore and analyze the Netflix Movies and TV Shows dataset to identify trends, patterns, missing values, and useful insights.

## 🎯 Objectives

- Understand the structure of the Netflix dataset
- Perform data cleaning and preprocessing
- Identify and handle missing values
- Detect duplicate records
- Analyze Movies and TV Shows
- Analyze ratings, countries, and genres
- Study release-year trends
- Analyze movie durations and TV show seasons
- Identify meaningful patterns and insights
- Create visualizations to communicate findings

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📂 Dataset

The dataset contains information about Netflix Movies and TV Shows.

### Dataset Features

- `show_id` – Unique identifier
- `type` – Movie or TV Show
- `title` – Title of the content
- `director` – Director of the content
- `cast` – Cast members
- `country` – Country of production
- `date_added` – Date added to Netflix
- `release_year` – Original release year
- `rating` – Content rating
- `duration` – Movie duration or number of TV seasons
- `listed_in` – Genre/category
- `description` – Content description

## 🔍 EDA Performed

### 1. Data Understanding

- Checked number of rows and columns
- Examined column names
- Checked data types
- Generated basic statistical summaries

### 2. Missing Value Analysis

Missing values were identified in columns such as:

- Director
- Cast
- Country
- Date Added
- Rating
- Duration

Missing categorical values were handled using appropriate placeholder values instead of unnecessarily deleting records.

### 3. Duplicate Analysis

Duplicate records were checked and no duplicate rows were found.

### 4. Content Type Analysis

Movies and TV Shows were compared to understand their distribution on Netflix.

### 5. Release Trend Analysis

The distribution of Netflix titles across different release years was analyzed.

### 6. Rating Analysis

The most common content ratings available on Netflix were identified.

### 7. Country Analysis

Countries contributing the highest number of Netflix titles were analyzed.

### 8. Genre Analysis

The most frequently occurring Netflix genres were identified.

### 9. Movie Duration Analysis

Movie durations were extracted and analyzed in minutes.

### 10. TV Show Season Analysis

The number of seasons available for TV Shows was analyzed.

### 11. Content Addition Trend

The number of titles added to Netflix over different years was analyzed.

### 12. Anomaly Analysis

Older release years were examined to identify unusual patterns in the dataset.

### 13. Hypothesis Analysis

The distribution of Movies and TV Shows was compared using statistical values and visualization.

## 📊 Visualizations

The project includes visualizations for:

- Movies vs TV Shows
- Movies vs TV Shows percentage distribution
- Release-year trends
- Movies vs TV Shows release trend
- Content ratings
- Top countries
- Top genres
- Movie duration distribution
- TV show seasons
- Netflix content added over the years
- Top release years
- Missing values analysis

All visualization images are stored in the `visualizations` folder.

## 💡 Key Insights

- Netflix contains more Movies than TV Shows.
- Movies account for approximately **69.62%** of the dataset, while TV Shows account for approximately **30.38%**.
- Missing values were mainly observed in the **Director, Cast, and Country** columns.
- The dataset contains **no duplicate records**.
- Release-year analysis shows changes in Netflix content distribution across different years.
- Rating analysis identifies the most common content ratings.
- Country and genre analysis highlights the major contributors and content categories.
- Movie duration analysis provides insights into the distribution of movie lengths.
- TV Show season analysis shows the distribution of the number of seasons.
- Content addition analysis shows how Netflix content changed over different years.

## 📁 Project Structure

```text
CodeAlpha_EDA/
│
├── EDA_Netflix.ipynb
├── netflix_titles.csv
├── README.md
│
└── visualizations/
    ├── missing_values.png
    ├── movies_vs_tv_shows_hypothesis.png
    ├── movies_vs_tv_shows.png
    ├── release_trend.png
    ├── movies_vs_tv_shows_release_trend.png
    ├── top_ratings.png
    ├── top_countries.png
    ├── top_genres.png
    ├── movie_duration_distribution.png
    ├── tv_show_seasons.png
    ├── content_added_trend.png
    ├── top_release_years.png
    └── movies_vs_tv_shows_pie.png