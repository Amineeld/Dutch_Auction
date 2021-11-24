from brownie import accounts, DutchAuction

def deploy_ducth_auction():
    account = accounts[0]
    DutchAuction.deploy({"from":account})

    

def main():
    deploy_ducth_auction()