import requests
import time
from datetime import datetime
#Task-2  Extract the Fields
# URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}
# 🔹 Category keywords
category_keywords = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Store results
category_data = {cat: [] for cat in category_keywords}

#  Fetch top story IDs
try:
    res = requests.get(TOP_STORIES_URL, headers=headers)
    res.raise_for_status()
    story_ids = res.json()[:200]
except requests.exceptions.RequestException as e:
    print("Failed to fetch IDs:", e)
    story_ids = []

#  Function to assign category
def get_category(title):
    title = title.lower()
    for category, keywords in category_keywords.items():
        for word in keywords:
            if word in title:
                return category
    return None

#  Loop through stories
for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        
        if res.status_code != 200:
            print(f"Failed story {story_id}")
            continue
        
        story = res.json()
        title = story.get("title", "")

        category = get_category(title)
        
        # Skip if no category match
        if not category:
            continue
        
        # Limit 25 per category
        if len(category_data[category]) >= 25:
            continue

        # 🔹 Extract required fields
        record = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", ""),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        category_data[category].append(record)

        # Stop if all categories filled
        if all(len(category_data[c]) >= 25 for c in category_data):
            break

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {story_id}:", e)
        continue

#  Sleep per category (as required earlier)
for _ in category_data:
    time.sleep(2)

# Combine all data
final_data = []
for cat in category_data:
    final_data.extend(category_data[cat])

print("Total records collected:", len(final_data))

import os
import json
#task 3 Save to a JSON File 
# Step 1: Create folder if it doesn't exist
folder_name = "data"
os.makedirs(folder_name, exist_ok=True)

#  Step 2: Create filename with today's date
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"{folder_name}/trends_{date_str}.json"

#  Step 3: Save data to JSON file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4)

#  Step 4: Print summary
print(f"Collected {len(final_data)} stories. Saved to {file_path}")

#output 
#task-2 data processing
#Total records collected: 67
#Task-3 save data to json
#Collected 67 stories. Saved to data/trends_20260408.json