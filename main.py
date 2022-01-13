import requests
import json

# API docs: https://www.coingecko.com/en/api/documentation
class py_coingecko:
    base_url = "https://api.coingecko.com/api/v3"
    ping_url = f"{base_url}/ping"

    # ---------------ping-----------
    # check API server status
    def ping(self):
        r = requests.get(self.ping_url)
        return json.loads(r.content)

    # --------------simple------------
    def get_name(self, ticker=""):
        list_url = f'{self.base_url}/coins/list'
        r = requests.get(list_url)
        r_json = json.loads(r.content)

        return [item for item in r_json if item['symbol'] == ticker][0]['id']

    def price(self, name='bitcoin', currency='usd'):
        price_url = f'{self.base_url}/simple/price?ids={name}&vs_currencies={currency}'
        r = requests.get(price_url)
        r_json = json.loads(r.content)
        return r_json[name][currency]

    # -------------coins-----------
    # def id(self, name):
    #     params = [['localization', 'false'],
    #               ['tickers', 'false'],
    #               ['market_data', 'true'],
    #               ['community_data', 'false'],
    #               ['developer_data', 'false'],
    #               ['sparkline', 'false']]
    #
    #     price_url = f'{self.base_url}/coins/{name}?'
    #
    #     for key, value in params:
    #         if not value:
    #             price_url = f'{price_url}&{key}={value}'
    #
    #     r = requests.get(price_url)
    #     r_json = json.loads(r.content)
    #
    #     return r_json['market_data']['current_price']['usd']

coingecko = py_coingecko()

# btc_price = coingecko.price('bitcoin')
# eth_price = coingecko.price('ethereum')
#
# print(btc_price)
# print(eth_price)

# print(coingecko.get_name('btc'))

# allocations
day_trading = 0.1
long_term = 0.45
short_term = 0.4
options = 0.05

cur_day_trading = ['looks']
cur_long_term = ['btc', 'eth', 'luna', 'atom', 'yfi']
cur_short_term = ['ftm', 'near', 'btrfly', 'cvx', 'crv', 'fxs']

# TODO: list individual balances in each token, then calculate allocations

