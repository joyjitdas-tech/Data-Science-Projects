#import all library
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

#load data set
df = pd.read_csv("anime_dataset.csv")



# --- 1. Missing values check ---
print("\nMissing values in each column:")
print(df.isnull().sum())


# --- 2. Distribution of scores by anime type ---
plt.figure(figsize=(10,6))
sns.boxplot(x='type', y='score', data=df)
plt.title('Score Distribution by Anime Type')
plt.show()


# --- 3. Number of anime released per year ---
plt.figure(figsize=(12,6))
df['year'] = df['year'].fillna(0).astype(int)  # Handle missing years
release_counts = df[df['year'] > 1900]['year'].value_counts().sort_index()
release_counts.plot(kind='bar')
plt.title('Number of Anime Released per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# --- 4. Average score over years ---
avg_score_year = df.groupby('year')['score'].mean()
plt.figure(figsize=(12,6))
avg_score_year.plot()
plt.title('Average Anime Score Over Years')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.show()


# --- 5. Status distribution (Finished, Airing, etc.) ---
plt.figure(figsize=(8,5))
sns.countplot(y='status', data=df, order=df['status'].value_counts().index)
plt.title('Anime Status Distribution')
plt.show()


# --- 6. Popular ratings (age restrictions) ---
plt.figure(figsize=(8,5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Anime Rating Distribution')
plt.show()


# --- 7. Duration cleaning and analysis ---
# Extract numeric duration (in minutes) from 'duration' strings like '24 min per ep'
def extract_duration(x):
    try:
        return int(x.split(' ')[0])
    except:
        return None

df['duration_min'] = df['duration'].apply(extract_duration)
# print(df.head(1))
plt.figure(figsize=(8,5))
sns.histplot(df['duration_min'].dropna(), bins=30)
plt.title('Distribution of Episode Duration (minutes)')
plt.xlabel('Duration (min)')
plt.ylabel('Count')
plt.show()


# --- 8. Top studios producing anime ---
# Studios is a list of studios, let's flatten and count top studios
studios_flat = []
for studios_list in df['studios'].dropna():
    # Assume studios are string representations of lists, convert safely
    if isinstance(studios_list, str):
        try:
            studios = eval(studios_list)
            studios_flat.extend(studios)
        except:
            pass
    elif isinstance(studios_list, list):
        studios_flat.extend(studios_list)

studio_counts = Counter(studios_flat)
top_studios = studio_counts.most_common(10)

studios_names, studios_freq = zip(*top_studios)
plt.figure(figsize=(10,6))
sns.barplot(x=studios_freq, y=studios_names)
plt.title('Top 10 Anime Studios by Number of Anime Produced')
plt.xlabel('Count')
plt.show()


# --- 9. Relationship between score and episodes ---
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='episodes', y='score', alpha=0.5)
plt.title('Score vs Number of Episodes')
plt.xlabel('Number of Episodes')
plt.ylabel('Score')
plt.show()

# some changes in dataframe
# Episodes - fill missing with median (or any suitable value)
df['episodes'] = df['episodes'].fillna(df['episodes'].median())

# Score - you can fill with median
df['score'] = df['score'].fillna(df['score'].median())

# Type - fill with most frequent type
df['type'] = df['type'].fillna(df['type'].mode()[0])

# Rating - fill missing with 'Unknown'
df['rating'] = df['rating'].fillna('Unknown')

# print(df.info())
# print(df.shape)

# Save changes to CSV file (no inplace argument here)
df.to_csv('anime_dataset.csv', index=False)