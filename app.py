import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

response = requests.get(url)
data = response.json()

print("Bitcoin Price:", data["bitcoin"]["usd"], "USD")
print("Ethereum Price:", data["ethereum"]["usd"], "USD")