import pandas as pd 
from collections import defaultdict

# •	Loads a CSV
# •	Removes rows with missing values
# •	Creates a derived column using a list comprehension
# •	Returns a summary dictionary using defaultdict or Counter

df = pd.read_csv("data/csv/amazon_books_reviews_sample_20k.csv")

total_rows = df.shape[0]

# Removes All Null Rows
df = df.dropna()

removed_rows = total_rows - df.shape[0]

print(df.columns)

# If not verified_purchase and rating less then Misleading review/rating

df["verified rating"] = list(zip(df["rating"],df["verified_purchase"]))

df["Misleading_rating"] = ["True" if (i[1]==False and i[0]>4.0) else "False" for i in df["verified rating"] ]

print(df[df["Misleading_rating"]=="True"].shape)

total_misleading_records = df[df["Misleading_rating"]=="True"].shape[0]


dictionary = {"total_rows":total_rows,"removed_rows":removed_rows,"total_misleading_records":total_misleading_records}

print(dictionary)

# df["WOM"] = df["date"]

