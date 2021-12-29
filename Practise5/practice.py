import json
from urllib.request import urlopen
from re import *
goods = { 1: {"Name": "Butter",
              "Price": 80,
              "Description": "yellow-to-white solid emulsion of fat globules"
              },
        2: {"Name": "Bread",
                      "Price": 40,
                      "Description": "White loaf baked with heat"
                      },
        3: {"Name": "Milk",
                      "Price": 72,
                      "Description": "Milky item for drinking"
                      },
        4: {"Name": "Cheese",
                      "Price": 280,
                      "Description": "Solid and yellow piece with holes"
                      },
        5: {"Name": "Salami",
                      "Price": 749,
                      "Description": "Made with meet and other chemical elements"
                      }}


with open("file.json", "w") as json_file:
    json.dump(goods, json_file, indent=4)

with open("file.json", "r") as json_file:
    file_json = json.load(json_file)

with urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as currency:
    money = currency.read()
    data_currency = json.loads(money)

with open("currency.json", "w") as currency_json_file:
    json.dump(data_currency, currency_json_file, indent=4)

def sum_in_currency(currency = "USD"):
    usd = int(data_currency["Valute"][currency]["Value"])
    sum = 0
    for dct in file_json.items():
        sum += int(dct[1]["Price"])
    print(f"Сумма в иностранной валюте {currency}", sum * usd)

sum_in_currency()