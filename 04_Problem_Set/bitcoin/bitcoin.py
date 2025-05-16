import sys
import requests
import json

API_KEY = "21df1b2c354d2a2989702056222e82a6c2dd875f0a12195753a540e5e1853c29"

BASE_URL = "https://rest.coincap.io/v3"
ASSET_SLUG = "bitcoin"
url = f"{BASE_URL}/assets/{ASSET_SLUG}"

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number.")
    sys.exit(1)

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}
# in this way we can pass the api key separetely called passing as headers with the requests.get method
# in that the url from which we get the data is separate and out api is separate


try:
    response = requests.get(url, headers=headers)

    api_data = response.json()

    usd = api_data['data']['priceUsd']
    usd = float(usd)
    final = n * usd
    print(f"{final:,.4f}")

except requests.RequestException as e:
    sys.exit(1)