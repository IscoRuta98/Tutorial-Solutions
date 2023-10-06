# Solution 2

## Aim

**Minimum requirement**: Create a Command-Line Interface (CLI) programme using Python that
does the following:

1. Generates Algorand account (i.e. public & private keys, and mnemonic phrase) for the
user if the user.
    - Transfer ALGOs from one account to another,
    - Make sure you print the Transaction ID so that the user can verify the transaction on the Algorand Test Net.
2. Creates an NFT for the user.
    - The user should enter the following arguments: sender address, unit name, asset
name, and a URL where more information about the asset can be retrieved.
    - Set the: manager, reserve, freeze, and callback parameters to the sender’s
address
    - The output should contain the Transaction ID.

Make sure the accounts are generated on the Algorand Test Network, and all transactions can
be viewed on Algorand’s Test Network.

**Challenge**: Instead of a python CLI, create a web based application. You can use tools covered in the tutorials, or any other tools you prefer.

 ## Helpful Resources
 - [Purestake API](https://developer.purestake.io/)
 - [Algorand Standard Assets (ASAs) Documentation](https://developer.algorand.org/docs/get-details/asa/)
 - [Build Command Line Interface with Python's argparse](https://realpython.com/command-line-interfaces-python-argparse/)


## Usage

The Algorand CLI offers two main functionalities, each with its respective command-line options:

1. **Generate Algorand Account and Transfer ALGOs**
    - To generate an Algorand account and transfer ALGOs, use the following command:
    ```
    python main.py generate-account --receiver-address RECEIVER_ADDRESS --amount AMOUNT
    ```
    - `generate-account`: Specifies the action to generate an Algorand account and transfer ALGOs.
    - `--receiver-address <RECEIVER_ADDRESS>`: The receiver's Algorand address (required).
--amount AMOUNT: The amount of ALGOs to transfer (in whole ALGOs, required).
After executing this command, the CLI will display the Transaction ID for verification.

2. **Create NFT (Non-Fungible Token)**
    - To create an NFT with customizable parameters, use the following command:
    ```
    python main.py create-nft --sender-address SENDER_ADDRESS --unit-name <UNIT_NAME> --asset-name <ASSET_NAME> --asset-url <ASSET_URL>
    ```
    - `create-nft`: Specifies the action to create an NFT.
    - `--sender-address <SENDER_ADDRESS>`: The sender's Algorand address (required).
    - `--unit-name <UNIT_NAME>`: The unit name for the NFT (required).
    - `--asset-name <ASSET_NAME>`: The asset name for the NFT (required).
    - `--asset-url <ASSET_URL>`: The URL where additional asset information can be retrieved (required).
    Upon successful execution, the CLI will display the Transaction ID for reference.

#### Transaction Verification
All transactions performed using the Algorand CLI can be verified on the Algorand Test Network. The Transaction ID provided after each operation allows users to track and confirm the transactions' status and details.