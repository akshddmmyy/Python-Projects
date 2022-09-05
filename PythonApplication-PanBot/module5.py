startno=0
size=ci.functions.getUserRoundsLength(add).call()

#mypublickeytrustwallet-
#New metamask
add=bchain.toChecksumAddress('')
mypvtkey=""

#write txn on pancakecontract
#build,sign and send transaction

myacbal=bchain.fromWei(node.eth.get_balance(add),'ether')
sendval=bchain.toWei(myacbal/15,'ether')
epoch=ci.functions.currentEpoch().call()

def betbear(add,sendval):
    size +=1
    nonce=node.eth.getTransactionCount(add)
    tx={
    'nonce':nonce,
    'from':add,
    'value':sendval,
    'gas':400000,
    'gasPrice':bchain.toWei('5','Gwei')
    }
    betting=ci.functions.betBear(epoch).buildTransaction(tx)
    signtxn=node.eth.account.sign_transaction(betting,mypvtkey)
    txnhash=node.eth.send_raw_transaction(signtxn.rawTransaction)
    return txnhash

def betbull(add,sendval):
    size +=1

    nonce=node.eth.getTransactionCount(add)
    tx={
    'nonce':nonce,
    'from':add,
    'value':sendval,
    'gas':400000,
    'gasPrice':bchain.toWei('5','Gwei')
    }
    betting=ci.functions.betBull(epoch).buildTransaction(tx)
    signtxn=node.eth.account.sign_transaction(betting,mypvtkey)
    txnhash=node.eth.send_raw_transaction(signtxn.rawTransaction)
    return txnhash


def claimreward(epochs):
    startno=ci.functions.getUserRoundsLength(add).call()
    nonce=node.eth.getTransactionCount(add)
    tx={
    'nonce':nonce,
    'from':add,
    'value':0,
    'gas':800000,
    'gasPrice':bchain.toWei('5','Gwei')
    }
    rewards=ci.functions.claim(epochs).buildTransaction(tx)
    signtxn=node.eth.account.sign_transaction(claim,mypvtkey)
    txnhash=node.eth.send_raw_transaction(signtxn.rawTransaction)
    return txnhash

#return data as list[0]-is a list of epochs entered
#list[1] is a list of tuples showing each epoch info as (up=0,down=1,amount i entered,Claimed or not)
def getuserrounds(startno,size):
    tempdict=ci.functions.getUserRounds(add,startno,size).call()
    return tempdict


#called once for each user.
def fetchclaimable():
    counter=-1
    epochs=[]
    userclaimable=getuserrounds(startno,size)
    for i in useuserclaimable[1]:
        counter+=1
        for j in i:
            if j[2]=='False':
                cepoch=i[0][counter]
                epochs.append(cepoch)

    size=0 #reinitializeing size variable.

    return epochs

def claimable(epochs):

    epochlength=len(epochs)

    for i in range(epochlength):
        temp=ci.functions.claimable(epochs[i],add).call()
        if(temp!='True'):
            epochs.pop(epochs[i])

    return epochs

def checkreciept(txnhash=""):
    try:
        tempdic=node.eth._get_transaction_receipt(txnhash)
        if(temdic['status']==1):
            print("Transaction Mined Succesfully")
        else:
            print("Transaction was reverted by EVM.")


    except:
        print("transaction Failed")
