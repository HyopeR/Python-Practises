import sys

import requests

# Json ve Döviz verilieri çekmek ve kullanmak.
# fixer.io

api_key = 'fac639744344b814594d43639e56a87a'
url = 'http://data.fixer.io/api/latest?access_key={}'.format(api_key)

base_currency = input("Base Currency:")
target_currency = input("Target Currency:")
amount_of_money = input("Amount of Money:")

response = requests.get(url)
currencies = response.json()

try:
    base_currency_price = currencies.get('rates', {}).get(str.upper(base_currency))
    target_currency_price = currencies.get('rates', {}).get(str.upper(target_currency))

    if base_currency_price is not None and target_currency_price is not None:
        result_price = float(target_currency_price) / float(base_currency_price)
        total_amount = float(amount_of_money) * result_price

        compare_currency_result = '1 {} = {} {}'.format(base_currency, result_price, target_currency)
        total_result = '{} {} = {} {}'.format(amount_of_money, base_currency, total_amount, target_currency)

        print(compare_currency_result)
        print(total_result)
    else:
        raise Exception("Invalid currency!")

except Exception as error:
    print(repr(error))


