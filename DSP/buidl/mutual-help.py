from pprint import pprint
from bitshares import BitShares
from bitshares.block import Block, BlockHeader
from ui import print_permissions, pprintOperation, print_table, print_tx
from bitsharesbase.operations import getOperationNameForId
from bitshares.account import Account
from bitsharesbase.account import PasswordKey

testnet = BitShares(
    "wss://node.testnet.bitshares.eu",
    rpcuser="vel-ma",
    rpcpassword = "P5J5vtQDEyFRMPyqgtTv6guw7W7nYKzHnqsqn8B2ALYpY",
    nobroadcast=False,
    bundle=True,
)


t = [["Account", "Amount"]]
accounts = ["vel-ma"]
for a in accounts:
  account = Account(a, bitshares_instance=testnet)
  for b in account.balances:
    t.append([str(a), str(b)])
  print_table(t)

testnet.wallet.unlock("P5J5vtQDEyFRMPyqgtTv6guw7W7nYKzHnqsqn8B2ALYpY")

print_tx(
        testnet.create_account(
          "mutual-insurance-fund-993", 
          registrar="vel-ma", 
          referrer="vel-ma",
          referrer_percent=50,
          owner_key=None,
          active_key=None,
          memo_key=None,
          owner_account="vel-ma",
          active_account=None,
          password="somethingstupid",
          additional_owner_keys=[],
          additional_active_keys=[],
          additional_owner_accounts=["vel-ma","oatrick1995"],
          additional_active_accounts=[],
          proxy_account="proxy-to-self",
          storekeys=True)
    )

testnet.broadcast()

##allow - change threashold
foreign_account = format(
            PasswordKey("mutual-insurance-fund-993", "somethingstupid", "active").get_public(), "TEST"
        )
print_tx(
        testnet.allow(
            foreign_account,
            weight=1,
            account="vel-ma",
            permission="active",
            threshold=2,
        )
    )


##transfer funds
print_tx(testnet.transfer("mutual-insurance-fund-993", 5, "TEST",  account=account))



##proposal - claim
##vote - vote

testnet.broadcast()