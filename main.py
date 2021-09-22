from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
rep = cg.get_coins_markets(vs_currency='usd')
print(report)

asd = int(input("Enter: "))
counter = 0
while counter < asd:
    counter += 1
    print(counter," - ", rep[counter]['name'], rep[counter]['market_cap'])
