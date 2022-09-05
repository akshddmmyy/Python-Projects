import pickle
#write data in file
def writedatatofile(blist,filename):
    filebase=filename
    with open("F:\\{}".format(filebase),'wb') as f:
        for i in blist:
            pickle.dump(i,f)
        print("done with ",i, "records")
    
#read data in file
def readatafromfile(filename):
    filebase=filename
    blist=[]
    with open("F:\\{}".format(filebase),'rb') as f:
        while True:
            try:
                blist.append(pickle.load(f))
            except EOFError:
                break
        
    return blist
        
    
