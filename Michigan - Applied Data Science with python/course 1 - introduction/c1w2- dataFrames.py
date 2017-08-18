# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 09:41:01 2017

@author: Polla
Michigan - Applied DS Course 1 week 2
"""
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

print(df.Cost)
print(df['Item Purchased'])
#df.Cost=df.Cost*0.2
#print(df.Cost)

#df['Cost'] *= 0.8
#print(df)

print("")
print("Querying DF")
print("solution1")
df2=df.where(df['Cost']>3).dropna()
#df2=df2.dropna()
print(df2.Name)
print("solution2")
print(df['Name'][df['Cost']>3])