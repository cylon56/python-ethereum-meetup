from web3 import Web3
import json

# Use Web3.py to connect to the Ethereum Blockchain
def create_connection(url):
    w3 = Web3(Web3.HTTPProvider(url))
    w3.isConnected()
    return w3

# Test our connection by printing the latest block info
def print_block_info(w3):
    print(w3.eth.getBlock('latest'))

# Create an instance of our service smart contract to communicate with
def create_delivery_service_connection(w3, address):
    with open("service_contract_abi.json", "r") as read_file:
        contract_abi = json.load(read_file)
    Contract = w3.eth.contract(abi=contract_abi)
    formatted_address = w3.toChecksumAddress(address)
    contract_instance = Contract(address=formatted_address)
    return contract_instance

# Call the smart contract for the status of a delivery (no transaction costs)
def check_delivery_status(contract):
    result = contract.functions.alice_delivered().call()
    print('The Delivery Status is: ' + str(result))

# Mark the delivery as complete (send a transaction to the smart contract)
def mark_delivered(contract, account):
    tx_hash = contract.functions.markDelivered(
        True).transact({'from': account})
    return tx_hash


w3 = create_connection('http://127.0.0.1:8545')
print_block_info(w3)

# delivery_contract = create_delivery_service_connection(w3, '0x7bd0690bf95a4b08501a2ca524d727f7cb4f69a0')
# check_delivery_status(delivery_contract)
# alice = get_account(w3)
# tx_result = mark_delivered(delivery_contract, w3.eth.accounts[1])
# print(str(w3.getTransactionReceipt(tx_result)))
# check_delivery_status(delivery_contract)
