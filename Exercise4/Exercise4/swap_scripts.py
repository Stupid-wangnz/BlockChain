from bitcoin.core.script import *

######################################################################
# This function will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret 
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
# 
# TODO: Fill this in to create a script that is redeemable by both
#       of the above conditions.
# 
# See this page for opcode: https://en.bitcoin.it/wiki/Script
#
#

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        # fill this in!
        
        #因为无论如何，要需要recipient的签名来兑现
        #所以首先验证recipient的签名
        public_key_recipient,
        OP_CHECKSIGVERIFY,
        
        #if is sender's sig
        OP_IF,
        public_key_sender,
        OP_CHECKSIG,
        #else 检查是否是hash of secret
        OP_ELSE,
        #必须用HASH160而不是256
        #因为alice初始化hash of secret时就是用的HASH160
        OP_HASH160,
        hash_of_secret,
        OP_EQUAL,
        OP_ENDIF
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        # fill this in!
        secret,
        OP_0,
        sig_recipient
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        # fill this in!
        sig_sender,
        OP_1,
        sig_recipient
    ]

#
#
######################################################################

