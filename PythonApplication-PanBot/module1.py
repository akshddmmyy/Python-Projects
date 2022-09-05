
from datetime import datetime as dt

#convert timestamp in a list of dictionary to human readable form
def converttimestamp(rlist):
    for i in rlist:
        for key in i.keys():
            if "Timestamp" in key:
                i[key]=str(dt.fromtimestamp(i[key]))
    return rlist

#get seconds from a timestamp
def seconds(time):
    return (time.strftime("%S"))

#getnth round data
def getrounddata(roundno):
    i=0
    static=roundno
    rounddict={"epoch":"", "startTimestamp":"", "lockTimestamp":"", "closeTimestamp":"", "lockPrice":"", "closePrice":"", "lockOracleId":"", "closeOracleId":"", "totalAmount":"", "bullAmount":"", "bearAmount":"", "rewardBaseCalAmount":"", "rewardAmount":"", "oracleCalled":""}
    rdata=ci.functions.rounds(static).call()       
    for key in rounddict.keys():
        rounddict[key]=rdata[i]
        i+=1
    return rounddict

#get last 30 seconds data of a round
def getrounddatalastseconds(roundno,closetimestamp):
    static=roundno
    nlist=[]
    flag=True
    while(flag):
        mytimestamp=dt.timestamp(dt.now())
        diff=(closetimestamp-mytimestamp)
        if (diff>=0 and diff<=30):
            rounddict= getrounddata(static)
            nlist.append(rounddict)
        elif diff<0:
            flag=False

    return nlist

