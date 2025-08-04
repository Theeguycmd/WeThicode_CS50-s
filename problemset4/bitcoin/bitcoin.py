import sys
import requests

def main():
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    header = {"Authorization" : "Bearer 74a9fcf326191a77da79c1efe309bbbd44557959dfb8083b70cc89825f691e0d"}
    if len(sys.argv) > 2:
        sys.exit("Expected two command-line argument")
    elif len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            amount = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            try:
                info = requests.get(url, headers=header)
            except requests.RequestException:
                pass
            else:
                one_bitcoin = float(info.json()["data"]["priceUsd"]) * amount
                print(f"$ {one_bitcoin:,.4f}")

if __name__ == "__main__":
    main()
