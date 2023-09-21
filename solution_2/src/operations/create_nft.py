from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod
from decouple import config


def create_nft(sender_secret_phrase: str, unit_name: str, asset_name: str):
    # Load the API key from the environment file
    api_key = config("API_KEY")
    # print(api_key)
    if not api_key:
        raise ValueError("API_KEY not found in environment")

    # example: ALGOD_CREATE_CLIENT
    # Create a new algod client, configured to connect to our local sandbox
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    headers = {"X-API-Key": api_key}
    algod_client = algod.AlgodClient(api_key, algod_address, headers)

    private_key = mnemonic.to_private_key(sender_secret_phrase)
    # print(f"Base64 encoded private key: {private_key}")
    address = account.address_from_private_key(private_key)
    print(f"Address: {address}")

    # Account 1 creates an NFT called `ESG` with a total supply
    # of 1 units and sets itself to the freeze/clawback/manager/reserve roles
    sp = algod_client.suggested_params()
    txn = transaction.AssetConfigTxn(
        sender=address,
        sp=sp,
        default_frozen=False,
        unit_name=unit_name,
        asset_name=asset_name,
        manager=address,
        reserve=address,
        freeze=address,
        clawback=address,
        total=1,
        decimals=0,
    )

    # Sign with secret key of creator
    stxn = txn.sign(private_key)
    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print(f"Sent asset create transaction with txid: {txid}")
