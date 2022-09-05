from datetime import datetime as dt

import module4

temp=module4.getrounddata(38070)

colist=[]
bolist=[]

while(True):
    ctime=dt.timestamp(dt.now())
    if(ctime>=temp['lockTimestamp']):
        ctempdict=module4.oraclefeeds()
        btempdict=module4.boraclefeeds()
        colist.append(ctempdict)
        bolist.append(btempdict)

    if(dt.timestamp(dt.now())>=temp['closeTimestamp']):
       print("stopped at",dt.now(),"while closetimestamp was ",dt.fromtimestamp(temp['closeTimestamp']))
       break

import module6
module6.writedatatofile(colist,"coracle5mindataforacompleteround")
module6.writedatatofile(bolist,"boracle5mindataforacompleteround")

#odict={'startedAt':"","updatedAt":"",'answer':""}
cflist=[]
for i in colist:
    if i['answer'] not in cflist:
        cflist.append(i['answer'])

bflist=[]
for i in bolist:
    if i['answer'] not in bflist:
        bflist.append(i['answer'])











    
    
