import asyncio
from datetime import datetime as dt
from datetime import timedelta

import time
from binance import AsyncClient, BinanceSocketManager
import csv

#apikey=""
#secretkey=""

f=open("G:\\4hourdata.csv","w",newline='')
fobj=csv.writer(f)
fobj.writerow(("OpenTime","Open","High","Low","Close","VOLUME","CloseTime","QuoteAssetVolume","NumberofTrades","TakerBuyBaseAssetVolume","TakerBuyQuoteAssetVolume","Ignore"))

async def kline_listener(client):
    endtime=1645950600000#int(dt.timestamp(dt.now())*1000)  ##27/2/2022 2 pm 
    starttime=1645921800000#int((dt.timestamp(dt.now() - timedelta(hours=4)))*1000)#27/2/2022 6 am
    #bm = BinanceSocketManager(client)
    #async with bm.get_historical_klines_generator#("bnbusdt",'1m',1643673600000,1644796800000,limit=1000,"SPOT") as stream:
       
    async for kline in await client.get_historical_klines_generator("BNBUSDT",AsyncClient.KLINE_INTERVAL_3MINUTE,starttime,endtime):
        fobj.writerow(kline)
        
    f.close()
    await client.close_connection()
    print("connection closed and returning")

    return 



async def start():
    global client
    client = await AsyncClient.create()
    await kline_listener(client)
    


def socketstart():
    asyncio.run(start())
   
socketstart()






