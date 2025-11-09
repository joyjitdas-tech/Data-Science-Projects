# Anime Dataset from MyAnimeList

This project contains a dataset of anime information collected from MyAnimeList using the [Jikan API](https://jikan.moe/). The dataset is used for performing Exploratory Data Analysis (EDA) to gain insights into anime trends, ratings, genres, and more.

---

## Dataset Description

- The dataset (`anime_dataset.csv`) includes information such as:
  - Anime titles
  - Scores and ratings
  - Genres
  - Number of episodes
  - Release dates
  - Popularity rankings
  - And other metadata available from MyAnimeList via the Jikan API

---

## Data Collection

- Data was collected programmatically using the Jikan API, a free and unofficial MyAnimeList RESTful API.
- The dataset was saved in CSV format for ease of analysis.

---

## Exploratory Data Analysis (EDA)

The goal of the EDA is to:
- Understand the distribution of anime scores and ratings.
- Analyze genre popularity.
- Explore trends over time, such as release years and episode counts.
- Identify correlations between different variables.

---

## How to Use

1. Clone this repository or download the dataset.
2. Load the dataset using pandas:
    ```python
    import pandas as pd
    anime = pd.read_csv('anime_dataset.csv')
    ```
3. Perform your preferred analysis or visualization using Python libraries like pandas, matplotlib, seaborn, etc.

---

## Dependencies

- Python 3.x
- pandas
- matplotlib
- seaborn
- requests (for API data collection)

---

## Contact

If you have any questions or suggestions, feel free to reach out!


