from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
ex3a_txout_scriptPubKey = [OP_2DUP,OP_ADD,2011,OP_EQUALVERIFY, OP_SUB, 269 ,OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00009
    txid_to_spend = (
        '0502ee78cda2cb28402348179afc35c4e142cb6bea8e8788e930e25b8e270318')
    utxo_index = 3
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
