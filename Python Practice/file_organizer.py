# Organise the Files by types in their own directory

# Get Raw directory and check files types
# Loop the raw directory 
# Get file as item and move it to 'extension'/ if extension file does not exist then create it

import shutil
import os

raw_dir = "data/raw_files"

def file_organiser(raw_dir):

    files_list_path = [raw_dir+"/"+i for i in os.listdir(raw_dir)]

    msg = []
    for f in files_list_path:
        # print(f)
        ext = f.split(".")[-1]
        dir = raw_dir.split('/')[0]+"/"+ext
        if not os.path.exists(dir):
            os.makedirs(dir)

        try:
            shutil.move(f,dir)
            (f"File '{f}' successfully moved to '{dir}'")
        except Exception as e: 

            print(f"Error found : {e}")

    return "Done"

'''Thoughtprocess for the entire Code Below'''

# files_list = os.listdir(raw_dir)

# now I can create a each item with raw_dir + /files_name 
files_list_path = [raw_dir+"/"+i for i in os.listdir(raw_dir)]

# for i in files_list:
#     files_list_path.append(raw_dir+"/"+i)

# shutil lib is used to move files 
# print(files_list_path[0],"data"+"/txt/"+files_list[0])

# This works now need to make it dynamic and add try except to catch errors 

# Create makedir for unique files extensions

# ext_dir = [raw_dir.split("/")[0]+'/'+ i for i in list(set([i.split('.')[1] for i in files_list]))]

#print(ext_dir)

# for dir in ext_dir:
#     # If dir does not exist then mkdir or else dont
#     if not os.path.exists(dir):
#         print(os.makedirs(dir))
#         # os.mkdir(dir)

def file_organiser(raw_dir):

    files_list_path = [raw_dir+"/"+i for i in os.listdir(raw_dir)]

    msg = []
    for f in files_list_path:
        # print(f)
        ext = f.split(".")[-1]
        dir = raw_dir.split('/')[0]+"/"+ext
        if not os.path.exists(dir):
            os.makedirs(dir)

        try:
            shutil.move(f,dir)
            (f"File '{f}' successfully moved to '{dir}'")
        except Exception as e: 

            print(f"Error found : {e}")

    return "Done"


if __name__=="__main__":
    file_organiser(raw_dir)

# shutil.move(files_list_path[0],"data"+"/txt/"+files_list[0])
