import numpy as np
import pandas as pd
import requests
import math
from scipy.stats import percentileofscore as score
import xlsxwriter

name = 'Austere Command'
api_url = f'https://api.scryfall.com/catalog/card-names'
data = requests.get(api_url).json()
data

card_name = data["data"]

for cards in card_name:
    print(cards)


def get_card_names():
  card_name = data["data"]
  for cards in card_name:
    save_data.append(cards)

save_data = []
get_card_names()
save_data

df = pd.DataFrame(save_data, columns=["Card Name"])
print(df)
# type(df)

writer = pd.ExcelWriter('cards.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Cards', index=False)

writer.save()
