# 区块链练习二

**2011269 王楠舟 计算机科学与技术**

## 练习内容

（a） 生成一个涉及四方的多签名交易，这样交易可以由第一方（银行）与另外三方（客户）中的任何一方（客户）共同赎回，而不仅仅只是客户或银行。对于这个问题，你可以假设是银行的角色，这样银行的私钥就是你的私钥，而银行的公钥就是你的公钥。使用 keygen.py生成客户密钥并将它们粘贴到 ex2a.py 中。

（b）赎回事务并确保 scriptPubKey 尽可能小。可以使用任何合法的签名组合来赎回交易至 faucet 地址，但要确保所有组合都有效。

## 实现关键代码

由于银行的签名必须确认，锁定脚本中需要对银行签名做单独认证，所以前两项分别是银行的公钥，即`my_public_key`，以及`OP_CHECKSIGVERIFY`操作码，用于对栈中的公钥和签名进行认证，由于我们不希望认证完银行签名后就退出，还要继续对客户签名做多方认证，所以不使用`OP_CHECKSIG`；

对于一个多方签名认证，`OP_N`指定总人数，`OP_M`指定需要认证的签名数，在中间压入三个客户的公钥，最后`OP_CHECKMULTISIG`进入多方认证。

```python
ex2a_txout_scriptPubKey = [
    my_public_key,
    OP_CHECKSIGVERIFY,
    OP_1,
    cust1_public_key,
    cust2_public_key,
    cust3_public_key,
    OP_3,
    OP_CHECKMULTISIG
]
```

在解锁脚本中，需要注意我们比特币中的栈结构，因为我们在锁定脚本中是先认证银行签名，再认证客户签名，所以锁定脚本里先压入客户签名再压入银行签名，保证银行签名在栈顶。

```python
def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)

    return [
        OP_0,
        cust2_sig,
        bank_sig
    ]
```

在这里我们用二号用户的签名进行认证。`OP_0`是`OP_CHECKMULTISIG`的一个bug，会多弹栈一次，所以我们只需要随便压入一个内容占位就行，该位置的内容不需要具体含义。