# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:28:01 2022

@author: Benk
"""
import pandas as pd
from pandasql import sqldf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------Belleabeat datat=set-----------------------------
df = pd.read_csv('marketing_data.csv')
df.head()
#------------------Removing duplicated features--------------------------------
print('size of the original  dataframe: ',df.shape)
Rdf=df.T.drop_duplicates().T
ListRemovColumns=list(set(df) - set(df))
print('List Of the  duplicated features wich are removed now ')
print(ListRemovColumns)
df=Rdf
print('duplicated features removed, new data size: ',df.shape)

#------------------Removing duplicated samples (The same observation of differents )-----
duplicateObser = df[df.duplicated()]
LabelsDupObser=duplicateObser.axes[0].tolist()
print('Number of duplicated observations:', duplicateObser.shape[0])
print('List of the duplicated Observations', LabelsDupObser)

#------------------check number of missing values-----------------
print(" \nCount total NaN at each column in a DataFrame : \n\n",
df.isnull().sum())
#------------------Removing variables with more than 50% of missing values----
ThresholdMissVals=.5
pct_null = df.isnull().sum() / len(df)
missing_features = pct_null[pct_null >= ThresholdMissVals].index
df.drop(missing_features, axis=1, inplace=True)
print('missing values removed, new data size:', df.shape)

#df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
#------------------Filling The missing values of the variable Income with 0
# Fill NaN values with zero
df=df.fillna(0)
ColumnName=list(df.columns)

# Get unique values of a the column marital satue then replace 
# the  ones that doesnt make sense------
MaritalVal=df.Marital_Status.unique()
df.drop(df.loc[df['Marital_Status']=='Absurd'].index, inplace=True)
df.drop(df.loc[df['Marital_Status']=='YOLO'].index, inplace=True)
df['Marital_Status'] = df['Marital_Status'].replace(['Alone'],'Single')
df['Marital_Status'] = df['Marital_Status'].replace(['Together'],'Married')
MaritalVal=df.Marital_Status.unique()
print(MaritalVal)


# df= df.rename(columns={' Income ': 'Income'}, inplace=False)
# df= df.rename(columns={'Dt_Customer': 'DtCustomer'}, inplace=False)

# clean columns names (remove space)
df.columns = (df.columns.str.strip().str.upper()
              .str.replace(' ', '_')
              .str.replace('(', '')
              .str.replace(')', '')
              )
print('Columns cleanned, space removed')
#Getthe statistical description of the data to get 
# the variables who have potentiols outliers
MarketingDescrib=df.describe()[['INCOME', 'KIDHOME',
       'TEENHOME', 'RECENCY', 'MNTWINES', 'MNTFRUITS',
       'MNTMEATPRODUCTS', 'MNTFISHPRODUCTS', 'MNTSWEETPRODUCTS',
       'MNTGOLDPRODS', 'NUMDEALSPURCHASES', 'NUMWEBPURCHASES',
       'NUMCATALOGPURCHASES', 'NUMSTOREPURCHASES', 'NUMWEBVISITSMONTH']]   
# MarketingDescrib.to_csv('MarketingDescrib.csv')
#Based On the desciption file the INCOME variables has outliers

# Plot the income variables to define the threshold in order to remove 
# the outliers
sns.boxplot(df['INCOME'])
ListOutlierIndex=np.where(df['INCOME']>100000)
df.drop([140,  208,  323,  495,  525,  729,  830,  851, 1241, 1560, 1822,
        1921, 2200],inplace = True)
#Store the cleanned data
df.to_csv('CleanMarketing_data.csv')
# Add of columns of TotalPurchases using Excel