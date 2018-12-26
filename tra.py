# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:05:40 2018

@author: I355604
"""

import pandas as pd
import numpy as np
d=pd.read_csv('test.csv',encoding = "ISO-8859-1")
y=[]
d11=pd.read_csv('storedata.csv',encoding = "ISO-8859-1")
l=len(d)
l1=len(d)/len(d11)
l1=int(l1)

c=[]
cost=np.array(d11['COST'])
for x in range(l1):
    for y in cost:
        c.append(y)



loc=d['STOREID']
l=[]
for i in loc:
    l.append(i)

date=d['CURRENTTIMESTAMP']
product=d['PRODUCTID']


sold=d['CURRENTCAPACITY']-d['LOSTCAPACITY']-d['EXPIREDCAPACITY']-d['DESTROYEDCAPACITY']

#c=y1
d1=pd.DataFrame(data=date)
d2=pd.DataFrame(data=product)
#d3=pd.DataFrame(data=location,columns=['LOCATION'])
d4=pd.DataFrame(data=sold,columns=['SOLDCAPACITY'])
d5=pd.DataFrame(data=l,columns=['Location'])
d6=pd.DataFrame(data=c,columns=['Cost'])
result=pd.concat([d1,d2,d5,d4,d6], axis=1,join_axes=[d1.index])

result['REVENUE']=result['SOLDCAPACITY']*y
#result.drop(result.index[-1])

#result.drop(result.tail(25).index,inplace=True) 

#d4=pd.DataFrame(data=TotalSold)n
#d5=pd.DataFrame(data=d['TOTAlCOST'])
result.rename(columns={'CURRENTTIMESTAMP': 'Date', 'PRODUCTID': 'Product','SOLDCAPACITY':'TotalSold','REVENUE':'Revenue'}, inplace=True)
result.to_csv('maintrans.csv',index=False)
