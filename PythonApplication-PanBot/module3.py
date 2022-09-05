#to get data for n historical rounds of pancakeswap

def historicaldata(startround,endround):
    baseanalyzelist=[]
    j=startround
    k=endround
    while(j<=k):
        
        try:
            temp=module1.getrounddata(j)
            baseanalyzelist.append(rounddict)
            print("current fetched round no:",j)
            j+=1

        except Exception as e: 
            print(e)
            j+=1
            continue
    return baseanalyzelist
