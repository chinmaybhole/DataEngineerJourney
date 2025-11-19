# Convert json to csv file -> Use Pandas to read json and to_Csv

import pandas as pd
import glob
import os
import logging

def json_to_csv(output_path,input_file):

    # output_path = "data/csv/"

    # input_file = "data/json/"
    # Condition if they have only given specific file then files = that file
    # Else glob.glob 

    if not os.path.exists(input_file):
        logging.error("Path does not exists")


    if os.path.isfile(input_file):
        files = [input_file]
        
    else:
        files = glob.glob(input_file+"*.json")

    num_files = len(files)
    status = 0
    for file in files:

        file_name = file.split("/")[-1].split(".")[0]

        try:
            json_df = pd.read_json(file)
        # read to Csv 
            status+=1
            json_df.to_csv(output_path+file_name+".csv",index=False)
            print(f"{file_name}.csv successfully saved at {output_path}")

        except Exception as err: 
            # print(err)
            logging.error(f"Error is {err}")
            #status = False

    return logging.info(f"Successfully converted {status}/{num_files} files.")


output_path = "data/csv/"

input_file = "data/evf"

print(json_to_csv(output_path,input_file))