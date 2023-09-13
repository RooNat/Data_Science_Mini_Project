# This file does the same thing as the "Data_Processing.ipynb"
# It is just the version of .py file
# The details about codes are in the "Data_Processing.ipynb" file

import pandas as pd
import numpy as np
import os
import re
import fnmatch #to find the files which match a pattern


# Convert a list to dictionary
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


def check_state(bid, ask):
    if bid == 1 and ask == 0:
        return 'bid'
    elif bid == 0 and ask == 1:
        return 'ask'
    elif bid == 1 and ask == 1:
        return 'bid/ask'
    else:
        return 'Nan'


def Match_bid_ask(result, df):
    for index, rows in result.iterrows():
        # if index<10:
        #     print(rows.bid)
        bid_in = 0
        ask_in = 0
        match_array = np.array([rows.Price, rows.Qty])
        bid_array = np.array(rows.bid)
        ask_array = np.array(rows.ask)
        for i in bid_array:
            if np.array_equal(match_array, i):
                bid_in = 1
                break
            elif rows.Price == i[0]:
                index_df = df[df['Time'] == rows.Time].index.values
                df_bid = df.loc[index_df[0] + 1]["bid"]
                if np.any(np.isin(df_bid, rows.Price)):
                    for k in df_bid:
                        if k[0] == i[0] and k[1] < i[1]:
                            bid_in = 1
                            break
                else:
                    bid_in = 1
                    break

        for j in ask_array:
            if np.array_equal(match_array, j):
                ask_in = 1
                break
            elif rows.Price == j[0]:
                index_df = df[df['Time'] == rows.Time].index.values
                df_ask = df.loc[index_df[0] + 1]["ask"]
                if np.any(np.isin(df_ask, rows.Price)):
                    for k in df_ask:
                        if k[0] == j[0] and k[1] < j[1]:
                            ask_in = 1
                            break
                else:
                    ask_in = 1
                    break
        result.at[index, 'State'] = check_state(bid_in, ask_in)
    return result

def data_wrangling(LOBs_data,Tapes_data):
    # list to array
    New_data=[]
    test_lines=np.asarray(LOBs_data,dtype=object)
    for i in test_lines:
        every_line=[["Time",i[0]],["Encode",i[1]],i[2][0],i[2][1]]
        New_data.append(every_line)

    for i in New_data:
        i[0]=Convert(i[0])
        i[1]=Convert(i[1])
        i[2]=Convert(i[2])
        i[3]=Convert(i[3])
        i[0]=i[0]|i[1]|i[2]|i[3]

    New_data=np.delete(New_data,[1,2,3],1)
    data_test=New_data.flatten()
    data_test2=data_test.tolist()
    df=pd.DataFrame(data_test2)
    merge_table = pd.merge(Tapes_data,df, on='Time', how="inner")
    result=Match_bid_ask(merge_table,df)
    return result



columns_name=['Time','Price','Qty']
# Read all .csv file in Tapes folder
# get the name of .csv file
folder_path = "./Dataset/HSBC_Set01/Tapes/"
new_folder_path="./Processed_data/"
# define the prefix for the new file names
prefix = "New_"

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # read the csv file
        Tapedata = pd.read_csv(os.path.join(folder_path, filename),names=columns_name,header=None)
        Tapedata["State"]=" "
        name=os.path.splitext(filename)[0]
        pattern = r"\d{4}-\d{2}-\d{2}"
        match=re.search(pattern,name)
        if match:
            # print the matched date string
            Date_match=match.group(0)
            # read the single file
            LOBs_folder_path='./Dataset/HSBC_Set01/LOBS/'
            LOB_file=""
            for file in os.listdir(LOBs_folder_path):
                if fnmatch.fnmatch(file, f'*{Date_match}*') and file.endswith(".txt"):
                    LOB_file=file
                    break
            substring="Exch0"
            LOBdata=[]
            with open(os.path.join(LOBs_folder_path, LOB_file),'r') as f:
                for line in f:
                    # add quotation marks around the substring using an f-string
                    new_line = line.replace(substring, f'"{substring}"')
                    LOBdata.append(eval(new_line.strip('\n')))
            Result=data_wrangling(LOBdata,Tapedata)
            new_filename=prefix+name+".csv"
            Result.to_csv(os.path.join(new_folder_path, new_filename), index=False)

        else:
            print("No match found.")
