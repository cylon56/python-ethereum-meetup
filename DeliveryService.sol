contract DeliveryService {
    
	bool public alice_delivered;
	address payable public alice = 0xFc874a6d9b57709ADA2e6f9882c1377C61e2f8D4;
	address public buyer;
	
	constructor() payable public {
		require(msg.value == 10 ether); 		
		buyer = msg.sender; 
	}
	
	function markDelivered(bool status) public {
		require(msg.sender == alice);
		alice_delivered = true;
	}

	function sendPayment() public {
		require(alice_delivered && msg.sender == buyer);
		alice.transfer(10 ether);	
	}
}