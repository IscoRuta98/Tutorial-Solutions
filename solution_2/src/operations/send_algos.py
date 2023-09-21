from base64 import b64decode
import json
from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod
from decouple import config


def send_algos(receiver_address: str, amount: int, sender_secret_phrase: str):
    # Load the API key from the environment file
    api_key = config("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment")

    # Create a new algod client, configured to connect to our local sandbox
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    headers = {"X-API-Key": api_key}
    algod_client = algod.AlgodClient(api_key, algod_address, headers)

    private_key = mnemonic.to_private_key(sender_secret_phrase)
    # print(f"Base64 encoded private key: {private_key}")
    address = account.address_from_private_key(private_key)
    print(f"Address: {address}")

    # Build Transaction
    # grab suggested params from algod using client
    # includes things like suggested fee and first/last valid rounds

    amount_in_micro_algos = amount * 1000000
    params = algod_client.suggested_params()
    unsigned_txn = transaction.PaymentTxn(
        sender=address,
        sp=params,
        receiver=receiver_address,
        amt=amount_in_micro_algos,  # In MicroAlgos
        note="Transaction using the Purestake API",
    )

    # sign the transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit the transaction and get back a transaction id
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully submitted transaction with txID: {}".format(txid))

    # wait for confirmation
    txn_result = transaction.wait_for_confirmation(algod_client, txid, 4)

    print(f"Transaction information: {json.dumps(txn_result, indent=4)}")
    print(f"Decoded note: {b64decode(txn_result['txn']['txn']['note'])}")


send_algos(
    "NLDYFIBO72B2AXHO7G2NS4WP4W36H3FUY57ZQ62G67SBHFK5VGAUTMLMJY",
    2,
    "glance actor salon bridge enroll pepper ramp extra vintage galaxy head bamboo fall emotion reform credit blast surge found maximum problem gas giant able scheme",
)
