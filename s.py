# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:53:36 2018

@author: I355604
"""

import pandas as pd
import numpy as np
data1=pd.read_csv('allstore.csv')
data2=pd.read_csv('Product.csv',encoding = "ISO-8859-1")
cost=[]
name=[]
for index,row in data1.iterrows():
    for i1,row1 in data2.iterrows():
        if row['SKUID']==row1['SKUID']:
            cost.append(row1['COST'])
            name.append(row1['SKUID'])



d1=pd.DataFrame(data=cost,columns=['COST'])
d2=pd.DataFrame(data=name,columns=['SKUID'])
d3=pd.DataFrame(data=data1['STOREID'])
result=pd.concat([d1,d2,d3], axis=1,join_axes=[d1.index])

result.to_csv('storedata.csv',index=False)

