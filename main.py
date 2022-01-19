# list of coins and current amount
import positions as p
from py_coingecko import py_coingecko
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world!'


if __name__ == '__main__':
    app.run()

coingecko = py_coingecko()

tickers = []
for category in p.categories:
    tickers += [coin for coin in category]

names = coingecko.get_names(tickers)
prices = coingecko.prices(names)

i = 0
category_totals = []
for category in p.categories:
    cur_total = 0

    for coin in category:
        cur_total += prices[i] * category[coin]
        i += 1

    category_totals.append(cur_total)

total = 0
for i in category_totals:
    total += i

# print(tickers)
# print(prices)
print(f'total: ${total:.2f}')

print(f'short_term: ${category_totals[0]:.2f} percentage: {category_totals[0]/total:.2%}')
print(f'long_term: ${category_totals[1]:.2f} percentage: {category_totals[1]/total:.2%}')
print(f'day_trading: ${category_totals[2]:.2f} percentage: {category_totals[2]/total:.2%}')
print(f'options: ${category_totals[3]:.2f} percentage: {category_totals[3]/total:.2%}')
print(f'stables: ${category_totals[4]:.2f} percentage: {category_totals[4]/total:.2%}')


