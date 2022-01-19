import requests
import json

# API docs: https://www.coingecko.com/en/api/documentation
class py_coingecko:
    base_url = "https://api.coingecko.com/api/v3"
    ping_url = f"{base_url}/ping"

    # ---------------ping-----------
    # check API server status
    def ping(self):
        try:
            r = requests.get(self.ping_url)
            return json.loads(r.content)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    # --------------simple------------
    def get_names(self, tickers=None):
        if tickers == None:
            tickers = [""]

        list_url = f'{self.base_url}/coins/list'
        try:
            r = requests.get(list_url)
            r_json = json.loads(r.content)

            names = []
            for ticker in tickers:
                names.append([item for item in r_json if item['symbol'] == ticker][0]['id'])

            if len(tickers) == 1:
                return names[0]
            else:
                return names

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def prices(self, names=None, currency='usd'):
        if names is None:
            names = ['bitcoin']

        price_url = f'{self.base_url}/simple/price?ids={names[0]}'
        for name in names[1:]:
            price_url += f'%2C{name}'

        price_url += f'&vs_currencies={currency}'

        try:
            r = requests.get(price_url)
            r_json = json.loads(r.content)

            prices = []
            for name in names:
                prices.append(r_json[name][currency])

            if len(names) == 1:
                return prices[0]
            else:
                return prices
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

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