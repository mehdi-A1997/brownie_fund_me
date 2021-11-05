from brownie import network, MockV3Aggregator, accounts, config
from web3 import Web3

DECIMALS=8
STARTING_PRICE= 200000000000

FORKED_LOCAL_ENVIRONMENT=['mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVIROMENTS=["development","ganache-local"]

def get_account():
    # print(account)
    # account= accounts.load("mehdi-account")
    # print(account)
    # account= accounts.add(config["wallets"]["from_key"])
    # print (account)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
