import requests
from typing import List, Dict
import json

date_list = list()
value_list = list()
print("Type the year of IGP-M")
bc_year = input("Choice between 1989 to 2022: ")
bc_month = input("Choice between 1 to 12: ")

if len(bc_month) == 1:
    bc_month = f"0{bc_month}"

bc_url = requests.get(f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.{189}/dados?formato=json")
bc_url = bc_url.json()
counter = 0

for i in bc_url:
    x = bc_url[counter]['data']
    y = bc_url[counter]['valor']
    date_list.append(x)
    value_list.append(y)
    counter = counter + 1

search = date_list.index(f"01/{bc_month}/{bc_year}")

print(f"\nData: {date_list[search]}\nIndice: {value_list[search]}%")