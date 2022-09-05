from eth_account import Account

def keygen(pvkey):

    acct = Account.from_key(pvkey)
    return acct.address
