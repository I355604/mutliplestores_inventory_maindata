# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:00:18 2018

@author: I355604
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:08:06 2018

@author: I355604
"""
from datetime import datetime,timedelta
import pandas as pd
import numpy as np
data=pd.read_csv('storedata.csv')
#print(data)

"""for id in data.iterrows():
        s=datetime.strptime('2017-1-1 \t','%Y-%m-%d \t')
        e=datetime.strptime('2019-1-1 \t','%Y-%m-%d \t')

        daterange = pd.date_range(s,e)
        for i in daterange:
            print(i.strftime("%Y-%m-%d \t"))"""
            
d=[]
c={}
items=[]        
s=datetime.strftime(datetime.now(),'%Y-%m-%d')

e=datetime.strftime(datetime.now(), '%Y-%m-%d')

daterange = pd.date_range(s,e)
for i in daterange:
    d.append(i.strftime("%Y-%m-%d"))
"""for index,row in data.iterrows():
      c[row['SKUID']]=row['COST']"""


x=np.array(list(data['SKUID']))
y=np.array(d)
data1= np.transpose([np.tile(x,len(y)),np.repeat(y,len(x))])
z=data1.tolist()
l=len(data1)

storeid=data['STOREID']
store=[]

for i in range(731):
    for j in storeid:
        store.append(j)

#data2.to_csv('test.csv',sep = ',',index=False)
#print(data2)

loc=[]


onshelf=np.random.randint(low=50, high=60, size=l )

storagecapacity=np.random.randint(low=95, high=101, size=l )
intransitcapacity=storagecapacity
destroyedcapacity=np.random.randint(low=1, high=10,size=l)
lostcapacity=np.random.randint(low=2, high=6,size=l)
expiredcapacity=np.random.randint(low=5,high=10,size=l)
capacityunit=['KG' for x in range(l)]
currentcapacity=storagecapacity

for i in storeid:
    loc.append(i)

d1=pd.DataFrame(data = z, columns = ['PRODUCTID','CURRENTTIMESTAMP'])
d11=pd.DataFrame(data=store, columns=['STOREID'])
d2=pd.DataFrame(data = onshelf, columns = ['ONSHELFCAPACITY'])
d22=pd.DataFrame(data=storagecapacity,columns=['STORAGECAPACITY'])
d3=pd.DataFrame(data=intransitcapacity,columns=['INTRANSITCAPACITY'])
d4=pd.DataFrame(data=destroyedcapacity,columns=['DESTROYEDCAPACITY'])
d5=pd.DataFrame(data=lostcapacity,columns=['LOSTCAPACITY'])
d6=pd.DataFrame(data=expiredcapacity,columns=['EXPIREDCAPACITY'])
d7=pd.DataFrame(data=capacityunit,columns=['CAPACITYUNIT'])
d8=pd.DataFrame(data=currentcapacity,columns=['CURRENTCAPACITY'])
#d10=pd.DataFrame(data=sold*y1,columns=['REVENUE'])

d9=pd.DataFrame(data=store,columns=['PRODUCTLOCATION'])


result=pd.concat([d1,d11,d9,d2,d22,d3,d4,d5,d6,d7,d8], axis=1,join_axes=[d1.index])
result.to_csv('test.csv',index=False)