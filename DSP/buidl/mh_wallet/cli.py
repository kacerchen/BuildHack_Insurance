#!/usr/bin/env python3

import sys
import json
import click
import logging
from bitshares.transactionbuilder import TransactionBuilder, ProposalBuilder
from prettytable import PrettyTable
from ui import print_permissions, get_terminal, print_version
from decorators import onlineChain, offlineChain, unlockWallet
from bitshares.storage import get_default_config_store
from main import main
from bitsharesbase.account import PasswordKey

from ui import print_message, print_table, print_tx

log = logging.getLogger(__name__)
config = get_default_config_store()

@main.command()
@click.pass_context
@onlineChain
@click.argument("association_name", nargs=1, type=str)
@click.argument(
    "members",
    nargs=-1
)
@click.option(
    "--password",
    default="somethingstupid",
    help="Association founders",
)
@click.option(
    "--account",
    default=config["default_account"],
    help="Account to pay the registration fee",
)
@unlockWallet
def newassociation(ctx, association_name, account, password, members):
    """ Create a new account
    """
    members_arr = []
    members_arr.append(members)
    ctx.bitshares.create_account(
            association_name, 
            registrar="vel-ma", 
            referrer="vel-ma",
            referrer_percent=50,
            owner_key=None,
            active_key=None,
            memo_key=None,
            additional_owner_keys=[],
            additional_active_keys=[],
            additional_owner_accounts=members,
            additional_active_accounts=[],
            proxy_account="proxy-to-self",
            storekeys=True,
            password=password)
    
    foreign_account = format(
            PasswordKey(association_name, password, "active").get_public(), "TEST"
        )
    
    ctx.bitshares.allow(
            foreign_account,
            weight=1,
            account="vel-ma",
            permission="active",
            threshold= int((len(members_arr)/2)+1)
        )

@main.command()
@click.pass_context
@onlineChain
@click.option("--claim-expiration", type=int)
def send_claim(ctx, claim_expiration):
   
    proposalBuilder = ProposalBuilder("vel-ma", claim_expiration or 2 * 24 * 60 * 60)

    tx = TransactionBuilder(eval(proposalBuilder.json()), bitshares_instance=ctx.bitshares)
    tx.broadcast()
    print_tx(tx.json())


@main.command()
@click.pass_context
@offlineChain
@click.argument("key", type=str)
@click.argument("value", type=str)
def set(ctx, key, value):
    """ Set configuration parameters
    """
    if key == "default_account" and value[0] == "@":
        value = value[1:]
    ctx.bitshares.config[key] = value


@main.command()
@click.pass_context
@offlineChain
def configuration(ctx):
    """ Show configuration variables
    """
    t = [["Key", "Value"]]
    for key in ctx.bitshares.config:
        t.append([key, ctx.bitshares.config[key]])
    print_table(t)


@main.command()
@click.pass_context
@offlineChain
@click.argument("filename", required=False, type=click.File("r"))
@unlockWallet
def sign(ctx, filename):
    """ Sign a json-formatted transaction
    """
    if filename:
        tx = filename.read()
    else:
        tx = sys.stdin.read()
    tx = TransactionBuilder(eval(tx), bitshares_instance=ctx.bitshares)
    tx.appendMissingSignatures()
    tx.sign()
    print_tx(tx.json())


@main.command()
@click.pass_context
@onlineChain
@click.argument("filename", required=False, type=click.File("r"))
def broadcast(ctx, filename):
    """ Broadcast a json-formatted transaction
    """
    if filename:
        tx = filename.read()
    else:
        tx = sys.stdin.read()
    tx = TransactionBuilder(eval(tx), bitshares_instance=ctx.bitshares)
    tx.broadcast()
    print_tx(tx.json())


@main.command()
@click.option("--prefix", type=str, default="BTS", help="The refix to use")
@click.option("--num", type=int, default=1, help="The number of keys to derive")
def randomwif(prefix, num):
    """ Obtain a random private/public key pair
    """
    from bitsharesbase.account import PrivateKey

    t = [["wif", "pubkey"]]
    for n in range(0, num):
        wif = PrivateKey()
        t.append([str(wif), format(wif.pubkey, prefix)])
    print_table(t)


if __name__ == "__main__":
    main()
