import json
from web3 import Web3
from datetime import timedelta, datetime

infura_url = 'https://ropsten.infura.io/v3/a1b856fc34e24754bdf947bb1ca04432'

web3 = Web3(Web3.HTTPProvider(infura_url))
epoch_day = 86400
# # accounts = web3.eth.
# web3.eth.defaultAccount = web3.eth.accounts[0]
# print(accounts)
print(web3.isConnected())
# First
abi = json.loads('[{"inputs":[{"internalType":"string","name":"_firstName","type":"string"},{"internalType":"string","name":"_lastName","type":"string"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_expiration","type":"uint256"}],"name":"addDrivingLicence","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"indexes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"licences","outputs":[{"internalType":"string","name":"firstName","type":"string"},{"internalType":"string","name":"lastName","type":"string"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"expiration","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"status","outputs":[{"internalType":"enum DriverLicense.LicenseStatus","name":"","type":"uint8"}],"stateMutability":"view","type":"function"}]')
address = "0x186CeAD5BBb78497b60E04E0BA5A0Cb030ad43ef"

# Second
# abi = json.loads('[{"inputs":[{"internalType":"string","name":"_firstName","type":"string"},{"internalType":"string","name":"_lastName","type":"string"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_expiration","type":"uint256"}],"name":"addDrivingLicence","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getExpiration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getFirstName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getLastName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"indexes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"licences","outputs":[{"internalType":"string","name":"firstName","type":"string"},{"internalType":"string","name":"lastName","type":"string"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"expiration","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"status","outputs":[{"internalType":"enum DriverLicense.LicenseStatus","name":"","type":"uint8"}],"stateMutability":"view","type":"function"}]')
# address = '0x101AAA3710Eeba6F01B6545219b90B2C099599EC'

contract = web3.eth.contract(address=address, abi=abi)

print(contract)

print(contract.functions.isOwner().call())

print(contract.functions.count().call())

# print(contract.functions.addDrivingLicence("A", "B", 123456789,60).call())
# print(contract.functions.addDrivingLicence("C", "D", 987654321, 70).call())
# print(contract.functions.addDrivingLicence("E", "F", 147852369, 40).call())
# print(contract.functions.addDrivingLicence("G", "H", 369258147, 67).transact())
count = contract.functions.count().call()


def get_all_licences():
    global count
    count = contract.functions.count().call()
    result = []  # '#\tName\t\t\t\tID\t\t\t\tExpiration Date\n'
    for i in range(count):
        index = contract.functions.indexes(i+1).call()
        license = get_single_license(index)
        result.append(license)
        print(f'Licence #{i+1}:\n\t'
              f'Name:\t\t{result[i][0]}\n\t'
              f'ID:\t\t\t{result[i][1]}\n\t'
              f'Expires:\t{result[i][2]}')
    print('RESULT = ' + str(result))
    return result


def get_single_license(id):
    license = contract.functions.licences(id).call()
    name = f'{license[0]} {license[1]}'
    # print('Getting ID')
    id = license[2]
    # print('Getting expiration')
    expiration = datetime.fromtimestamp(license[3]).strftime("%d-%m-%Y")
    return [name, id, expiration]


def add_licence(first_name, last_name, id, expiration):
    contract.functions.addDrivingLicence(first_name, last_name, id, expiration).call()
