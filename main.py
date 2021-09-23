from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
crp = cg.get_coins_markets(vs_currency='usd')
print(crp)

asd = int(input("Enter: "))
counter = 0
while counter < asd:
    counter += 1
    print(counter," - ", crp[counter]['name'],crp[counter]['market_cap'])
