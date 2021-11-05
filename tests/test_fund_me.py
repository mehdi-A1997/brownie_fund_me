from brownie import network,exceptions,accounts
from scripts.deploy import fund_me
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIROMENTS
from scripts.deploy import fund_me
import pytest

def test_can_fund_and_withdraw():
    account= get_account()
    fund= fund_me()
    entrance_fee= fund.getEntranceFee()
    tx= fund.fund({"from": account, "value":entrance_fee})
    tx.wait(1)
    assert fund.addressToAmountFunded(account.address)==entrance_fee

    tx2= fund.withdraw({"from":account})
    tx2.wait(1)
    assert fund.addressToAmountFunded(account.address)==0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("only for local testing")
    fund= fund_me()
    bad_actor= accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund.withdraw({"from":bad_actor})
