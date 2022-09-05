import module4
import scrapy
import binancefetch
import threading
from datetime import datetime as dt
from datetime import timedelta
import pickle
import notify

runcount,chromelog=0,0

def writedatatofile(blist,filename):
    #blist is a list
    filebase=filename
    with open("G:\\{}".format(filebase),'ab+') as f:
        for i in blist:
            pickle.dump(i,f)
        #print("done with ",i, "records")

def newround():
    global tepoch
    tepoch=module4.epochno()
    betrounddata=module4.getrounddata(tepoch)
    basetime=betrounddata['lockTimestamp']
    return basetime

#just for test
def betbear(panvalue,binres):
    notify.pb.push_note("BetBear","Bet has been placed Successfully")
    print("bearcalled")
    betloglist=[tepoch,{"run_at":run_at,"bet_at":bet_at},panvalue[0],binres[0]]
    writedatatofile(betloglist,'betlog.dat')

#just for test
def betbull(panvalue,binres):
    notify.pb.push_note("BetBull","Bet has been placed Successfully")
    print("bullcalled")
    betloglist=[tepoch,{"run_at":run_at,"bet_at":bet_at},panvalue[0],binres[0]]
    writedatatofile(betloglist,'betlog.dat')



def mainthread():
    global runcount
    
    global run_at,bet_at,delay,betdelay,panvalue,binres

    temptime=newround()
    #print("will lock round at ", dt.fromtimestamp(temptime))
    run_at = dt.fromtimestamp(newround()) - timedelta(seconds=60)
   # print("will run at ",run_at)
    bet_at= dt.fromtimestamp(newround()) - timedelta(seconds=20)
    #print("will bet at ",bet_at)
    delay = (run_at-dt.now()).total_seconds()
    betdelay= (bet_at-dt.now()).total_seconds()
    
    if ( delay > 0):
        runcount += 1
        print("Main thread logic started count ",runcount)

        panvalue=[0]
        binres=[0]
        t1=threading.Timer(delay,scrapy.scrapedata,args=(bet_at,panvalue))
        t2=threading.Timer(delay,binancefetch.socketstart,args=(bet_at,binres))

        t1.start()
        t2.start()

        t1.join()
        t2.join()
        

        #while testing only
        panvalue[0]=float(panvalue[0].strip('$'))
        binres[0]=float(binres[0])
        if ((panvalue[0] - binres[0])> 0 ):
            if ((panvalue[0] - binres[0]) >= 0.5 ):
                betbear(panvalue,binres)
        else:
            if ((panvalue[0] - binres[0]) <= (-0.5) ):
                betbull(panvalue,binres)


try:

    def main():
    
        #baseinitializations
        #startingwebdriveronce
        x=scrapy.scrapeinitial()
        if x==1:
            chromelog=0
            print("Crome Session started")
            while True:
                mainthread()
        
        else:
            if(chromelog>5):
                raise Exception("chrome causing error")
            else:
                main()
    main()
except Exception as e:
    notify.pb.push_note(" Main Big Exception ",e)
    scrapy.driver.close()
    #binancefetch.socketstop()
        
 
   
 
 



