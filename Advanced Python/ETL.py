import pandas as pd 
from collections import defaultdict
import os

# Class ETL

class ETL():
    def __init__(self):
        self.df = None
        pass

    # •	load() → reads the CSV
    def load(self):
        print("Data loading")
        self.df = pd.read_csv("data/csv/amazon_books_reviews_sample_20k.csv")
        return self
        
	# •	clean() → removes invalid rows
    def clean(self):
        print("Removed null rows")
        df = self.df
        # print(df.shape)
        df = df.dropna()
        # print(df.shape)
        self.df = df
        return self

	# •	transform() → adds 2 derived columns
    def transform(self):
        print("transformation in progress..")
        df = self.df 
        # print(df.shape)
        df["verified rating"] = list(zip(df["rating"],df["verified_purchase"]))
        df["Misleading_rating"] = ["True" if (i[1]==False and i[0]>4.0) else "False" for i in df["verified rating"] ]
        self.df = df
        return self
    
	# •	save() → writes cleaned CSV to /tmp/ or local folder
    def save(self):
        if not os.path.exists("data/tmp"):
            os.makedirs("data/tmp")
        self.df.to_csv("data/tmp/etl.csv")
        
        return self




etl = ETL()

df_load = etl.load().clean().transform().save()

print(df_load)

# df = pd.read_csv("data/csv/amazon_books_reviews_sample_20k.csv")

# total_rows = df.shape[0]

# # Removes All Null Rows
# df = df.dropna()

# removed_rows = total_rows - df.shape[0]

# print(df.columns)

# # If not verified_purchase and rating less then Misleading review/rating

# df["verified rating"] = list(zip(df["rating"],df["verified_purchase"]))

# df["Misleading_rating"] = ["True" if (i[1]==False and i[0]>4.0) else "False" for i in df["verified rating"] ]

# print(df[df["Misleading_rating"]=="True"].shape)

# total_misleading_records = df[df["Misleading_rating"]=="True"].shape[0]


# dictionary = {"total_rows":total_rows,"removed_rows":removed_rows,"total_misleading_records":total_misleading_records}

# print(dictionary)