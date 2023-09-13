import pandas as pd
import numpy as np
import os

def Convert(a):
    it=iter(a)
    res_dct=dict(zip(it,it))
    return res_dct


def lob_to_df(LOBdata):
    New_data = []
    test_lines = np.asarray(LOBdata, dtype=object)

    for i in test_lines:
        every_line = [["Time", i[0]], ["Encode", i[1]], i[2][0], i[2][1]]
        New_data.append(every_line)

    for i in New_data:
        i[0] = Convert(i[0])
        i[1] = Convert(i[1])
        i[2] = Convert(i[2])
        i[3] = Convert(i[3])
        i[0] = i[0] | i[1] | i[2] | i[3]

    New_data = np.delete(New_data, [1, 2, 3], 1)
    data_test = New_data.flatten()
    data_test2 = data_test.tolist()

    df = pd.DataFrame(data_test2)
    df = df.set_index('Time')
    return df


def metric_data(df):
    Mid_price = []
    Quoted_spread = []
    Weighted_Mid_price = []
    Bid_best_p = []
    Ask_best_p = []
    Bid_best_v = []
    Ask_best_v = []
    for index, row in df.iterrows():
        bid_array = np.array(row.bid)
        ask_array = np.array(row.ask)
        try:
            bid_best_price = bid_array[0][0]
            ask_best_price = ask_array[0][0]
            Mid_price.append((bid_best_price + ask_best_price) / 2)
            Quoted_spread.append(ask_best_price - bid_best_price)

            bid_best_volume = bid_array[0][1]
            ask_best_volume = ask_array[0][1]
            I = bid_best_volume / (bid_best_volume + ask_best_volume)
            wmid = bid_best_price * (1 - I) + ask_best_price * I
            Weighted_Mid_price.append(wmid)
            Bid_best_p.append(bid_best_price)
            Bid_best_v.append(bid_best_volume)
            Ask_best_p.append(ask_best_price)
            Ask_best_v.append(ask_best_volume)
        except IndexError:
            if len(bid_array) == 0 and len(ask_array) == 0:
                Mid_price.append(0)
                Quoted_spread.append(0)
                Weighted_Mid_price.append(0)
                Bid_best_p.append(None)
                Bid_best_v.append(None)
                Ask_best_p.append(None)
                Ask_best_v.append(None)
            elif len(bid_array) == 0:
                ask_best_price = ask_array[0][0]
                ask_best_volume = ask_array[0][1]
                Mid_price.append(ask_best_price / 2)
                Quoted_spread.append(ask_best_price)
                Weighted_Mid_price.append(None)
                Ask_best_p.append(ask_best_price)
                Ask_best_v.append(ask_best_volume)
                Bid_best_p.append(None)
                Bid_best_v.append(None)
            else:
                bid_best_price = bid_array[0][0]
                bid_best_volume = bid_array[0][1]
                Mid_price.append(bid_best_price / 2)
                Quoted_spread.append(-bid_best_price)
                Weighted_Mid_price.append(None)
                Bid_best_p.append(bid_best_price)
                Bid_best_v.append(bid_best_volume)
                Ask_best_p.append(None)
                Ask_best_v.append(None)
    df.insert(1, "Quoted_spread", Quoted_spread)
    df.insert(2, "Mid_Price", Mid_price)
    df.insert(3, "Weighted_Mid_Price", Weighted_Mid_price)
    df.insert(4, "Best_bid_price", Bid_best_p)
    df.insert(5, "bid_volume", Bid_best_v)
    df.insert(6, "Best_ask_price", Ask_best_p)
    df.insert(7, "ask_volume", Ask_best_v)
    return df

def generate_index(max_level):
    levels=[]
    for i in range(max_level):
        levels.append("level"+str(i+1))
    iterables=[levels,['Bid','Ask'],['Price','Volume']]
    col_index=pd.MultiIndex.from_product(iterables)
    return col_index

def get_LOBdf(df, col_index):
    LOB_df=pd.DataFrame(columns=col_index, index=df.index)
    for index, row in df.iterrows():
        bid_array=np.array(row.bid)
        ask_array=np.array(row.ask)
        try:
            for i in range(len(bid_array)):
                level_in="level"+str(i+1)
                LOB_df.at[index,(level_in,"Bid","Price")]=bid_array[i][0]
                LOB_df.at[index,(level_in,"Bid","Volume")]=bid_array[i][1]
            for j in range(len(ask_array)):
                level_in="level"+str(j+1)
                LOB_df.at[index,(level_in,"Ask","Price")]=ask_array[j][0]
                LOB_df.at[index,(level_in,"Ask","Volume")]=ask_array[j][1]
            # print(index)
        except Exception as e:
            print(e)
    return LOB_df


folder_path="./Dataset/HSBC_Set01/LOBS/"
new_folder_path="./LOBs_Benchmark/"
prefix="Benchmark_"
substring="Exch0"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        LOBdata = []
        name = os.path.splitext(filename)[0]
        with open(os.path.join(folder_path, filename), 'r') as f:
            for line in f:
                new_line = line.replace(substring, f'"{substring}"')
                LOBdata.append(eval(new_line.strip('\n')))
        df = lob_to_df(LOBdata)
        df = metric_data(df)
        max_level = 15
        # for index, row in df.iterrows():
        #     level = max(len(row.bid), len(row.ask))
        #     if level >= max_level:
        #         max_level = level
        col_index = generate_index(max_level)
        LOB_df = get_LOBdf(df, col_index)
        merge_table = pd.merge(df, LOB_df, on='Time')
        merge_table.drop(['bid', 'ask'], axis=1)
        new_filename=prefix+name+".csv"
        merge_table.to_csv(os.path.join(new_folder_path, new_filename), index=False)
        print(new_filename)