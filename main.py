from bs4 import BeautifulSoup

import requests
import json

# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
headers = {
    'Accept': '*/*',
    'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
# all_products = soup.find_all(class_='uk-grid uk-grid-medium')
# for product in all_products:
#     product_text = product.text.replace(' ', '')
#     product_href = product.get('href')
#     print(f'{product_text}:  {product_href}')

# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
# all_categories_dict = {}
# for product in all_products_hrefs:
#     product_text = product.text
#     product_href = 'https://health-diet.ru' + product.get('href')
#     all_categories_dict[product_text] = product_href
# with open("all_categories_dict_new.json", 'w') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
with open('all_categories_dict_new.json') as file:
    all_categories = json.load(file)
__id = 0
for category_name, category_href in all_categories.items():

    if __id == 0:
        rep = [",", " ", "-", "'"]
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, '_')

        print(category_name, category_href)
