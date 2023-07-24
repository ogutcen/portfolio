# LIBRARIES

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

import warnings
warnings.filterwarnings('ignore')


# Display settings for tables. Useful while debuging/testing the code.

pd.set_option('display.max_columns', None)

#pd.set_option('display.max_rows', None)

pd.set_option('display.max_rows', 160)
#pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', None)

def getDuplicateColumns(df):
 
    # Create an empty set
    duplicateColumnNames = set()
 
    # Iterate through all the columns
    # of dataframe
    for x in range(df.shape[1]):
 
        # Take column at xth index.
        col = df.iloc[:, x]
 
        # Iterate through all the columns in
        # DataFrame from (x + 1)th index to
        # last index
        for y in range(x + 1, df.shape[1]):
 
            # Take column at yth index.
            otherCol = df.iloc[:, y]
 
            # Check if two columns at x & y
            # index are equal or not,
            # if equal then adding
            # to the set
            if col.equals(otherCol):
                duplicateColumnNames.add(df.columns.values[y])
 
    # Return list of unique column names
    # whose contents are duplicates.
    return list(duplicateColumnNames)

df_excel=("filename.xlsx",,sheetname="sheet1")
df=pd.read.csv("filename.csv")
#Ayni tur tablolari ust uste birlestir.
df_all = pd.concat([df_1, df_2,df_3], axis=0)

#Sutun isim listesi
column_dict = {"eski sutun ismi" : "Yeni sutun Ismi"}
#Sonra sutun isim listesini uygulayalim.
df.df.rename(columns=column_dict)
#istedigin kadar karakteri bastan kes
df["atanan sutun"] = df["istenen sutun"].str[:4]

df.drop(columns=["dusurmek istedigim sutun"],axis=1,inplace=True)

Farkli uzunluktaki listeleri farkli kolonlarin unique degerleri aldiktan sonra birlestirip bir tablo yapmak ve bunu excele cikti almak.
from itertools import zip_longest
df_list1 = df_all['Hedef Sutun'].unique()
df_list1.sort()
df_list2 = df_all['2inci Hedef Sutun'].unique()
df_list2.sort()
# Hatta bir sutun icinde integer. string kairisik degerler olsun.
df_list3 = df_all['3uncu Hedef Sutun'].unique()
sorted(map(str, df_list3))

padded_lists = list(zip_longest(df_list1, df_list2, df_list3, fillvalue=None))

data = {'df_list1': [item[0] for item in padded_lists],
        'df_list2': [item[1] for item in padded_lists],
        'df_list3': [item[2] for item in padded_lists],












































