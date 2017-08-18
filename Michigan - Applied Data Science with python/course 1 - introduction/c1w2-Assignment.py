# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:24:20 2017

@author: Polla

Michigan - Applied DS Course 1 week 2 - Assignment
"""

#Part 1

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
#print(df.head())

#Question 0
def answer_zero():
    return df.iloc[0]
answer_zero() 


#Question 1
print("Question 1")
def answer_one():
    #max(df['Gold'])
    #df['Gold'][df['Gold']==max(df['Gold'])]
    df2=df.where(df['Gold']==max(df['Gold'])).dropna()
    return  df2.index[0]

print(answer_one())

print("")

#Question 2
print("Question 2")
def answer_two():
    df['difference']=df['Gold']-df['Gold.1']
    df2=df.where(df['difference']==max(df['difference'])).dropna()
    return  df2.index[0]

print(answer_two())

print("")

#Question 3
print("Question 3")
def answer_three():
    dfnew=df[(df['Gold']>=1) & (df['Gold.1']>=1)].dropna()
    dfnew['Totaldifference']=((dfnew['Gold']-dfnew['Gold.1'])/dfnew['Combined total'])
    df2=dfnew[dfnew['Totaldifference']==max(dfnew['Totaldifference'])]
    return  df2.index[0]

print(answer_three())

print("")

#Question 4
print("Question 4")
def answer_four():
    df['Points']=df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2']
    return  df['Points']

print(answer_four())

print("")