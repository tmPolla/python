# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:29:37 2017

@author: Polla

Michigan - Applied DS Course 1 week 2

1) Reindex the purchase records DataFrame to be indexed hierarchically, first by store
then by person.
2) Name these indexes Location and Name, 
3) Then add a new entry to it with the values of 
Name 'Kevyn', ItemPurch: 'Kitty Food', Cost: 3.00 Location:'Store2'

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


print("original")
print(df)
print("")

df['Location']=df.index
df=df.set_index(['Location','Name'])
print(df)

print("")
purchase_4 = pd.DataFrame({
                        'Cost': 3.00,
                        'Item Purchased': 'Kitty Food'},
                        index=['Store2','Kevyn']
                        )
print(purchase_4)
df=df.append(purchase_4)
print(df)

print("")
print("official solution")
df_origi = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df_origi = df_origi.set_index([df_origi.index, 'Name'])
df_origi.index.names = ['Location', 'Name']
df_origi = df_origi.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print(df_origi)