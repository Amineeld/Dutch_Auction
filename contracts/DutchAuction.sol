// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

import "contracts/SafeMath.sol";

contract DutchAuction {
    
    using SafeMath for uint256;

    //static
    uint256 public initialPrice = 10000;
    uint256 public endDate=block.timestamp + 10;
    uint256 public startDate = block.timestamp;

    address payable public seller;
    address payable winnerAddress;

    function bid() public payable {
        // Set usefull variables
        uint256 timeElapsed = endDate - block.timestamp;
        uint256 currentPrice = timeElapsed * initialPrice / (endDate - startDate );
        uint256 userBid = msg.value;

        // require to check if the auction has not ended or if the bid is big enough
        require(winnerAddress == address(0)); // check if someone has already claim and win the auction
        require(timeElapsed < endDate);
        require(userBid > currentPrice, "Bid is lower than current price");

        //Making the transfer
        winnerAddress = payable(msg.sender);
        winnerAddress.transfer(userBid - currentPrice); //refund the difference
        seller.transfer(currentPrice);

    }
    
   
    function getCurrentPrice() public view returns(uint256){

        return  (endDate - block.timestamp ) * initialPrice / (endDate-startDate);
    }

    function getWinnerAddress() public view returns(address){

        return  winnerAddress;
    }
}

