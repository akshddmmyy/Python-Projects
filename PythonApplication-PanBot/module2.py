
#start analyze
#0-no deviation, 1 deviation,2 eqal side of bear and bull
def analyzedata(baseanalyzelist):

    finalanalyzelist=[]

    for x in baseanalyzelist:
        adlist={"roundno":"","GreaterBetAmount":"","whowin":"","deviation":""}
        adlist['roundno']=x['epoch']
        adlist['GreaterBetAmount']=(max(x['bearAmount'],x['bullAmount']))*math.pow(10,-18)
    
        if(x['rewardBaseCalAmount']==x['bearAmount']):
            adlist['whowin']="Bear"

            if(x['bearAmount']>x['bullAmount']):
                adlist['deviation']=0

            elif(x['bearAmount']<x['bullAmount']):
                adlist['deviation']=1

            else:
                adlist['deviation']=2

        elif(x['rewardBaseCalAmount']==x['bullAmount']):
            adlist['whowin']="Bull"

            if(x['bearAmount']>x['bullAmount']):
                adlist['deviation']=1

            elif(x['bearAmount']<x['bullAmount']):
                adlist['deviation']=0

            else:
            
                adlist['deviation']=2
        
        else:
            adlist['whowin']="None"

        finalanalyzelist.append(adlist)

    return finalanalyzelist

#probability
def stats(blist):
    temp=[]
    beartotal,bulltotal,nonetotal=0,0,0
    duce,majority,minority=0,0,0
    for i in blist:
        if(i['whowin']=='Bear'):
            beartotal +=1
        elif(i['whowin']=='Bull'):
            bulltotal +=1
        else:
            nonetotal +=1

        if(i['deviation']==0):
            majority +=1
        elif(i['deviation']==1):
            minority +=1
        else:
           duce +=1
    temp={"TotalBullWins":bulltotal,"TotalBearWins":beartotal,"TotalNoneWins":nonetotal,"MajorityWins":majority,"MajorityProbability":majority/len(blist),"MinorityWins":minority,"MinorityProbability":minority/len(blist),"duce":duce}
    return temp


    