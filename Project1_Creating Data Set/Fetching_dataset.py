import requests
import time
import pandas as pd

def get_all_anime_data():
    all_data = []
    page = 1

    while True:
        url = f"https://api.jikan.moe/v4/anime?page={page}"
        print(f"Fetching page {page}...")
        #Try & except block
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error {response.status_code}, waiting before retry...")
                time.sleep(3)
                continue

            data = response.json()

            # Extract anime data
            for anime in data.get("data", []):
                all_data.append({
                    "title": anime.get("title"),
                    "episodes": anime.get("episodes"),
                    "score": anime.get("score"),
                    "year": anime.get("year"),
                    "type": anime.get("type"),
                    "status": anime.get("status"),
                    "rating": anime.get("rating"),
                    "duration": anime.get("duration"),
                    "genres": [g["name"] for g in anime.get("genres", [])],
                    "studios": [s["name"] for s in anime.get("studios", [])]
                })

            # Check if there’s a next page
            pagination = data.get("pagination", {})
            if not pagination.get("has_next_page", False):
                print(" All pages fetched successfully!")
                break

            # Move to next page
            page += 1
            time.sleep(0.5)  

        except Exception as e:
            print(f" Error on page {page}: {e}")
            time.sleep(3)

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(all_data)
    df.to_csv("anime_dataset.csv", index=False)
    print(f"\n Done! Saved {len(df)} anime to anime_dataset.csv")

# Run the func
get_all_anime_data()
