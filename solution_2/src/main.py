import argparse
from operations.generate_account import generate_keys
from operations.send_algos import send_algos
from operations.create_nft import create_nft


def main():
    parser = argparse.ArgumentParser(description="=Algorand CLI")
    parser.add_argument(
        "--option",
        "-o",
        type=str,
        required=True,
        choices=["generate-key-pair", "create-nft", "send-algos"],
        help="Choose an option: 1 for Algorand keypair generation, 2 for NFT creation, 3 Send ALGOs",
    )
    parser.add_argument(
        "--output", "-out", type=str, default=None, help="Output file for keys"
    )

    # Add arguments for send_algos function
    parser.add_argument(
        "--receiver-address", type=str, help="Receiver's Algorand address"
    )
    parser.add_argument(
        "--amount", type=int, help="Amount of ALGOs to send (in whole ALGOs)"
    )
    parser.add_argument(
        "--sender-secret-phrase", type=str, help="Sender's secret phrase"
    )

    parser.add_argument("--unit-name", type=str, help="Unit name for the NFT")

    parser.add_argument("--asset-name", type=str, help="Asset name for the NFT")

    args = parser.parse_args()

    if args.option == "generate-key-pair":
        private_key, address, secret_phrase = generate_keys()
        print("Algorand Address:", address)
        print("Private Key:", private_key)
        print("Secret Phrase:", secret_phrase)
        print("DO NOT SHARE YOUR PRIVATE KEY NOR SECRET PHRASE WITH ANYONE")
        if args.output:
            with open(args.output, "w") as f:
                f.write(f"Algorand Address: {address}\n")
                f.write(f"Private Key: {private_key}\n")
                f.write(f"Secret Phrase: {secret_phrase}\n")
    elif args.option == "create-nft":
        if not (args.sender_secret_phrase and args.unit_name and args.asset_name):
            print("Error: Missing required arguments for create-nft.")
            parser.print_help()
            return
        create_nft(args.sender_secret_phrase, args.unit_name, args.asset_name)
    elif args.option == "send-algos":
        if not (args.receiver_address and args.amount and args.sender_secret_phrase):
            print("Error: Missing required arguments for send-algos.")
            parser.print_help()
            return
        send_algos(args.receiver_address, args.amount, args.sender_secret_phrase)
    else:
        print(
            "Invalid option. Please choose 'generate-key-pair', 'create-nft', or 'send-algos'."
        )


if __name__ == "__main__":
    main()
