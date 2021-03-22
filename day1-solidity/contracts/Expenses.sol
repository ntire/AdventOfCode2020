pragma solidity ^0.5.0;

contract Expenses {
    address public owner;

    constructor() public {
        owner = msg.sender;
    }

    function find2020(uint[] memory expenses) public pure returns(uint) {
        for (uint i=0; i<expenses.length-1;i++) {
            for (uint k=i+1;k<expenses.length;k++) {
                if (expenses[i] + expenses[k] == 2020) {
                    return expenses[i] * expenses[k];
                }
            }
        }
        return 0;
    }

}