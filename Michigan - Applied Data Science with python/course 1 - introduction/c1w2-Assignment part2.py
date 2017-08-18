# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:46:44 2017

@author: Polla
Michigan - Applied DS Course 1 week 2 - Assignment Part 2
"""
import pandas as pd

census_df = pd.read_csv('census.csv')
#print(census_df.head())



#Question 5
#Which state has the most counties in it? 
#(hint: consider the sumlevel key carefully! You'll need this for future questions too...)
print("Question 5")
def answer_five():
    df=census_df[(census_df['SUMLEV']==50)].dropna()
    df2=df.groupby(['STNAME']).agg(['count'])['SUMLEV']
    df_result=df2.where(df2['count']==max(df2['count'])).dropna()
    return df_result.index[0]

answer_five()
#print(answer_five())

print("")

#Question 6-1
print("Question 6")
#Only looking at the three most populous counties for each state, 
#what are the three most populous states (in order of highest population 
#to lowest population)? Use CENSUS2010POP.
def answer_six_1():
    df=census_df[(census_df['SUMLEV']==50)].dropna()
    df = df.sort_values(['STNAME', 'CENSUS2010POP'], ascending=[True, False])
    groups=df['STNAME'].unique()
    resultdf = pd.DataFrame()
    for st in groups:
        grdf=df.where(df['STNAME']==st).nlargest(3, columns=['CENSUS2010POP']).loc[:, 'STNAME':'CENSUS2010POP']
#        grdf=grdf.nlargest(3, columns=['CENSUS2010POP']).loc[:, 'STNAME':'CENSUS2010POP']
#        grdf=grdf.loc[:, 'STNAME':'CENSUS2010POP']
        resultdf=resultdf.append(grdf)
#        print(grdf)
    resultdf=resultdf.sort_values(['CENSUS2010POP'], ascending=[False])
#    print(resultdf)
    resultList=[]
    resultdf=resultdf['STNAME']
#    for label, value in resultdf.head(3).iteritems():
    for label, value in resultdf.iteritems():
        resultList.append(value)
    
    return resultList
#    return True

#print(answer_six_1())
answer_six_1()

print("")

#Question 6
print("Question 6")
#Only looking at the three most populous counties for each state, 
#what are the three most populous states (in order of highest population 
#to lowest population)? Use CENSUS2010POP.
# First you find the top 3 counties in each state, 
# then you sum these 3 up separately for each state, 
# then you sort by those state sums, and you return 
# the top 3 state names by that sum.
def answer_six():
    df=census_df[(census_df['SUMLEV']==50)].dropna()
    df = df.sort_values(['STNAME', 'CENSUS2010POP'], ascending=[True, False])
    groups=df['STNAME'].unique()
    groupdf = pd.DataFrame()
    for st in groups:
        grdf=df.where(df['STNAME']==st).nlargest(3, columns=['CENSUS2010POP']).loc[:, 'STNAME':'CENSUS2010POP']
#        grdf=grdf.nlargest(3, columns=['CENSUS2010POP']).loc[:, 'STNAME':'CENSUS2010POP']
#        grdf=grdf.loc[:, 'STNAME':'CENSUS2010POP']
        groupdf=groupdf.append(grdf)
#        print(grdf)
    groupdf=groupdf.sort_values(['STNAME'], ascending=[False])
#    print(groupdf)
#    print("")
    sumdf = pd.DataFrame()

#    for st in groups:
    sumdf=groupdf.groupby(['STNAME'])[['CENSUS2010POP']].sum()
    sumdf=sumdf.sort_values(['CENSUS2010POP'], ascending=[False])
#        sumdf=sumdf.append(grdf)
#    sumdf=sumdf.sort_values(['CENSUS2010POP'], ascending=[False])
    resultList=[]
    for i in range(0,3):
        value=sumdf.index[i]
        resultList.append(value)

    return resultList


#print(answer_six())
answer_six()

print("")

#Question 7
print("Question 7")
#Which county has had the largest absolute change in population within the period 2010-2015? 
#
#(Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, 
# you need to consider all six columns.)
#
#e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, 
#then its largest change in the period would be |130-80| = 50.
def answer_seven():
    df=census_df[(census_df['SUMLEV']==50)].dropna()
    measuredValList=['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    df=df.loc[:, ['CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
    df['minimum'] = df.loc[:, measuredValList].min(axis=1)
    df['maximum'] = df.loc[:, measuredValList].max(axis=1)
    df['difference'] = df['maximum']-df['minimum']
    df['difference']=df['difference'].abs()
    df = df.sort_values(['difference'], ascending=[False])
#    result=df.head(1)['CTYNAME']
    for label, value in df.head(1)['CTYNAME'].iteritems():
        result=value
    return result

answer_seven()
#print(answer_seven())


print("")

#Question 8
print("Question 8")
#In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, 
#whose name starts with 'Washington', and whose POPESTIMATE2015 was greater 
#than their POPESTIMATE 2014.
#
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] 
#and the same index ID as the census_df (sorted ascending by index).

def answer_eight():
    df=census_df[(census_df['SUMLEV']==50)].dropna()
    df=df[(census_df['REGION']==1) | (df['REGION']==2)].dropna()
    df=df[df['CTYNAME'].str.contains('Washington', na = False)]
    df=df[(df['POPESTIMATE2015']>df['POPESTIMATE2014'])].dropna()
    df.sort_index(inplace=True)
    resultdf=df.loc[:,['STNAME', 'CTYNAME']]
    return resultdf

answer_eight()