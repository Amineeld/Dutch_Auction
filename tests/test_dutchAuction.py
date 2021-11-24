from brownie import accounts, DutchAuction, exceptions, rpc
import pytest, time

def test_deploy():
    #Arrange
    account = accounts[0]
    #Act
    dutch_auction = DutchAuction.deploy({"from":account})
    start_price = dutch_auction.getCurrentPrice()
    expected = 10000
    
    #Assert
    assert start_price == expected
    
def test_place_a_winning_bid():
    #Arrange
    account = accounts[0]
    account_bidder1 = accounts[1]

    #Act
    dutch_auction = DutchAuction.deploy({"from":account})


    dutch_auction.bid({"from":account_bidder1, "value":100000})
    #Assert
    assert account_bidder1 == dutch_auction.getWinnerAddress()
    
def test_place_a_bid_not_big_enough():
    #Arrange
    account = accounts[0]
    account_bidder1 = accounts[1]

    #Act
    dutch_auction = DutchAuction.deploy({"from":account})
    #transaction = dutch_auction.bid({"from":account, "value":100000})
    #Assert
    with pytest.raises(exceptions.VirtualMachineError):
        dutch_auction.bid({"from":account_bidder1, "value":9000})
    
def test_place_a_bid_after_one_already_won_the_auction():
    #Arrange
    account = accounts[0]
    account_bidder1 = accounts[1]
    account_bidder2 = accounts[2]
    #Act
    dutch_auction = DutchAuction.deploy({"from":account})
    dutch_auction.bid({"from":account_bidder1, "value":100000})
    #Assert
    with pytest.raises(exceptions.VirtualMachineError):
        dutch_auction.bid({"from":account_bidder2, "value":9000})
        
def test_place_a_bid_after_the_end_of_the_auction():
    #Arrange
    account = accounts[0]
    account_bidder1 = accounts[1]
    #Act
    dutch_auction = DutchAuction.deploy({"from":account})
    time.sleep(30)
    #Assert
    with pytest.raises(exceptions.VirtualMachineError):
        dutch_auction.bid({"from":account_bidder1, "value":9000})