from algosdk import account, mnemonic


def generate_keys():
    private_key, address = account.generate_account()
    secret_phrase = mnemonic.from_private_key(private_key)
    return private_key, address, secret_phrase


print(generate_keys())
