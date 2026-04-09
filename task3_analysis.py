import pandas as pd
#1 Load and Explore 
#  Load CSV
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

#  First 5 rows
print("First 5 rows:")
print(df.head())

#  Shape
print("\nShape of DataFrame:", df.shape)

#  Averages
print("\nAverage score:", df["score"].mean())
print("Average num_comments:", df["num_comments"].mean())


# 2- Basic Analysis with NumPy 
import numpy as np
# Convert columns to NumPy arrays
scores = df["score"].values
comments = df["num_comments"].values

#  Mean, Median, Std
print("\nScore Statistics:")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard Deviation:", np.std(scores))

#  Highest & Lowest Score
print("\nHighest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))

#  Category with most stories
top_category = df["category"].value_counts().idxmax()
print("\nCategory with most stories:", top_category)

#  Story with most comments
max_comments_index = np.argmax(comments)
top_story = df.iloc[max_comments_index]

print("\nStory with most comments:")
print("Title:", top_story["title"])
print("Comments:", top_story["num_comments"])
# 3- Add New Columns
#  Engagement column
df["engagement"] = df["num_comments"] / (df["score"] + 1)

#  Average score
avg_score = df["score"].mean()

#  is_popular column
df["is_popular"] = df["score"] > avg_score

# Preview
print(df.head())

#4-Save the result
#  Engagement column
df["engagement"] = df["num_comments"] / (df["score"] + 1)

#  Average score
avg_score = df["score"].mean()

#  is_popular column
df["is_popular"] = df["score"] > avg_score

# Preview
print(df.head())