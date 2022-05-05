# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:06:04 2022

@author: Benk
"""
import pandas as pd
from pandasql import sqldf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------Belleabeat datat=set-----------------------------
df = pd.read_csv('CleanMarketing_data.csv')
df.head()

CorrelMat= df.corr()
# stocks = CorrelMat.index.values
# CorrelMat = np.asmatrix(CorrelMat)
# CorrelMat[abs(CorrelMat) < .15] = 0
CorrWebPurchage=CorrelMat['NUMWEBPURCHASES']
print(CorrWebPurchage)
CorrWebPurchage=CorrWebPurchage**2
CorrWebPurchage.to_csv('CorrelationToWebPurchage.csv')
