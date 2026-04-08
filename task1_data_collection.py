import requests
import time
#Task 1 make API calls 
# Base URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories (for later grouping)
categories = ["technology", "worldnews", "sports", "science", "entertainment"]

# Store stories
category_stories = {cat: [] for cat in categories}

#  Step 1: Fetch top story IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    response.raise_for_status()
    story_ids = response.json()[:100]
except requests.exceptions.RequestException as e:
    print("Failed to fetch top stories:", e)
    story_ids = []

# 🔹 Step 2: Loop category-wise (as per requirement)
for category in categories:
    print(f"\nProcessing category: {category}")

    for story_id in story_ids:
        try:
            url = ITEM_URL.format(story_id)
            res = requests.get(url, headers=headers)

            if res.status_code != 200:
                print(f"Failed to fetch story {story_id}")
                continue

            story = res.json()

            # Safely extract title
            title = story.get("title", "")

            # (Categorization will be done later — just storing now)
            category_stories[category].append({
                "id": story_id,
                "title": title
            })
            

        except requests.exceptions.RequestException as e:
            print(f"Error fetching story {story_id}:", e)
            continue

    # 🔹 Required: Wait 2 seconds AFTER each category loop
    time.sleep(2)

print("\nFinished fetching stories.")
#output :

#Processing category: technology

#Processing category: worldnews

#Processing category: sports

#Processing category: science

#Processing category: entertainment

#Finished fetching stories.