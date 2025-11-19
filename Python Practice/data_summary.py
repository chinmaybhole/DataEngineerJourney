# got Csv files and summarize the files into one Data_summary.csv 

# Columns : filename, rows, cols, null_values, num_cols(list of numeric columns)

# Using Glob.glob to read all the csv file

import glob
import pandas as pd
import os
# Got both the files

dir_csv = "data/csv/*.csv"


# filenames = [i.split("/")[-1] for i in files]
def data_summary(dir_csv):

    files = glob.glob(dir_csv)
    out_dict = {"file_name":[],"rows":[],"cols":[],"null_values":[],"num_cols_list":[]}

    # out_dict = dict()
    for idx,i in enumerate(files):

        index = idx
        file_name = files[idx].split("/")[-1]
        # print(filenames)
        df = pd.read_csv(files[idx])

        rows = df.shape[0]

        cols = df.shape[1]

        null_values = df.isnull().sum().sum()
        # print(null_cols)
        # break

        num_cols_list = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

        # out_dict["index"].append(idx)
        out_dict["file_name"].append(file_name)
        out_dict["rows"].append(rows)
        out_dict['cols'].append(cols)
        out_dict['null_values'].append(null_values)
        out_dict['num_cols_list'].append(num_cols_list)

        # out_dict.appendx()
        # print(f"file_name : {file_name},rows :{rows}, cols : {cols}, null_cols : {null_cols},num_cols_list = {num_cols_list}")


    output_df = pd.DataFrame.from_dict(out_dict)
    if not os.path.exists("data/outputs/"):
        os.makedirs("data/outputs/")
    try:
        output_df.to_csv("data/outputs/summary_report.csv")
        print("Summary report generated: data/outputs/summary_report.csv")

    except Exception as e:
        print(f"Error occured : {e}")
    # print(df.isnull().sum().sum())

    return output_df
# Summarize it to give me Summarized Columns 

print(data_summary(dir_csv))
# print(df.head())