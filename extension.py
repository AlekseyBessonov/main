import json
import requests
from config import currency

class ConversionExcepion(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def converter(input_val):
        quote, base, amount = input_val
        try:
            quote_val = currency[quote]
        except KeyError:
            raise ConversionExcepion(f'Нет такой валюты {quote}')

        try:
            base_val = currency[base]
        except KeyError:
            raise ConversionExcepion(f'Нет такой валюты {base}')

        if quote == base:
            raise ConversionExcepion(f'Одинаковые валюты. Введите разные валюты!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionExcepion(f'Количество валюты должно быть числом, больше нуля. Вы вели {amount}')

        r = requests.get(
            f'https://free.currconv.com/api/v7/convert?apiKey=cd2ff852330c08894153&q={quote_val}_{base_val}&compact=ultra')
        api_format = f'{quote_val}_{base_val}'
        total_base = float(json.loads(r.content)[api_format]) * float(amount)
        text = f' За {amount} {quote} сейчас дают  {total_base:.2f} {base}'
        return text