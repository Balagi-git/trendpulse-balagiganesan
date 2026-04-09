import pandas as pd
#Step 1 — Load the CSV
# Load analysed data
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

print("Loaded rows:", len(df))
#Step 2 — Create outputs/ Folder
import os

# Create folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

print("Outputs folder ready")

import pandas as pd
#Step 1 — Load the CSV
# Load analysed data
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

print("Loaded rows:", len(df))
#Step 2 — Create outputs/ Folder
import os

# Create folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

print("Outputs folder ready")

#Step 3 — Use plt.savefig() Correctly
import matplotlib.pyplot as plt

# Example: Score distribution
plt.hist(df["score"], bins=20)

# Save FIRST
plt.savefig("outputs/score_distribution.png")

# Then show
plt.show()

import matplotlib.pyplot as plt

#  Get top 10 stories by score
top10 = df.sort_values(by="score", ascending=False).head(10)

#  Shorten titles (max 50 chars)
top10["short_title"] = top10["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

#  Create horizontal bar chart
plt.figure()
plt.barh(top10["short_title"], top10["score"])

# Reverse order so highest appears on top
plt.gca().invert_yaxis()

# Labels and title
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

#  Save BEFORE show
plt.savefig("outputs/chart1_top_stories.png")

plt.show()

#  Count stories per category
category_counts = df["category"].value_counts()

#  Create bar chart with different colors
plt.figure()
plt.bar(category_counts.index, category_counts.values)

# Labels and title
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

#  Save BEFORE show
plt.savefig("outputs/chart2_categories.png")

plt.show()

import matplotlib.pyplot as plt

#  Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

#  Create scatter plot
plt.figure()

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

#  Labels and title
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

#  Legend
plt.legend()

#  Save BEFORE show
plt.savefig("outputs/chart3_scatter.png")

plt.show()