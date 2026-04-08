import pandas as pd
import json
from datetime import datetime
#1 Load the JSON File
# 🔹 File path (adjust date if needed)
file_path = "data/trends_20260408.json"

# Load JSON file
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Print number of rows
print("Rows loaded:", len(df))

# output:Rows loaded: 67

#2 Clean the Data
#  1. Remove duplicates (based on post_id)
df = df.drop_duplicates(subset="post_id")

#  2. Handle missing values
df = df.dropna(subset=["post_id", "title", "score"])

#  3. Fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

#  4. Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]

#  5. Remove extra whitespace from title
df["title"] = df["title"].str.strip()

#  Final row count
print("Rows after cleaning:", len(df))
# Rows after cleaning: 63

#3.Save as CSV
#  Save cleaned DataFrame to CSV
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

#  Print confirmation message
print(f"Saved {len(df)} rows to {output_path}")

#  Print summary: stories per category
category_counts = df["category"].value_counts()

print("\nStories per category:")
print(category_counts)
# output:
#Saved 63 rows to data/trends_clean.csv

#Stories per category:
#category
#technology       23
#entertainment    18
#worldnews        11
#sports            8
#science           3
#Name: count, dtype: int64