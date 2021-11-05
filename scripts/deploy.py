from brownie import FundMe, accounts, MockV3Aggregator, config, network
from scripts.helpful_scripts import (
    FORKED_LOCAL_ENVIRONMENT,
    get_account,
    deploy_mock,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)
from web3 import Web3


def fund_me():
    account = get_account()

    # if we are on persistant network like rinkeby
    # otherwise deploy mock
    # pass priceFedd address to deploy
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        priceFeedAddress = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(fund_me.address)
    return fund_me


def main():
    fund_me()
