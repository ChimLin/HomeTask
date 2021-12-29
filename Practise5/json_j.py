import json

cars_json = """
    {"cars" : [ {"id" : 1,
                "title" : "Audi",
                "price" : "1000"
                },
                {"id" : 2,
                "title" : "VW",
                "price" : "1000"
                },
                {"id" : 3,
                "title" : "BMV",
                "price" : "1000"
                }

        ]
    }
"""

info = json.loads(cars_json)
print(f"{info['cars'][2]} продается в автосалоне")

# from url
import json
import pprint
from urllib.request import urlopen
pp = pprint.PrettyPrinter(indent=4)

# with urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as response:
#     source = response.read()
#
# data = json.loads(source)
# pp.pprint(data)

# print(data['Valute']['USD']['Value'])
#
# to_json = json.dump(info['cars'][2]['id'], ensure_ascii=false)
# print(to_json)

import json
from urllib.request import urlopen

goods = """
        { 1: {"Name": "Butter",
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
"""

json_object = json.loads(goods, indent=1)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)

to_json2 = json.loads(json_object)
print(to_json2)

with urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as currency:
    money = currency.read()

data_currency = json.loads(money)
price_dollar = data_currency['Valute']['USD']['Value']
sum = 0
