import asyncio
from datetime import datetime as dt
import time
from binance import AsyncClient, BinanceSocketManager

#apikey=""
#secretkey=""


async def kline_listener(client,bet_at,binres):
    bm = BinanceSocketManager(client)
    async with bm.kline_socket(symbol='BNBUSDT') as stream:
        while True:
            res = await stream.recv()
            binres[0]=res['k']['c']
            if(dt.now()>=bet_at):
                break

    await client.close_connection()
    print("connection closed")
    return 



async def start(bet_at,binres):
    global client
    client = await AsyncClient.create()
    await kline_listener(client,bet_at,binres)
    


def socketstart(bet_at,binres):
    asyncio.run(start(bet_at,binres))
   
async def socketstop():
    await client.close_connection()
    #print("connection closed")


