import random
from asyncio import sleep

from bs4 import BeautifulSoup
import requests
import json

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
url = 'https://tengrinews.kz/read/'
# req = requests.get(url, headers=headers)
#
# with open('projects.html', 'w', encoding='utf-8') as file:
#     file.write(req.text)
#
# with open('projects.html', encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# all_articles = soup.find_all(class_="tn-article-item")
# all_articles_dict = {}
# for article in all_articles:
#     if article.find('a'):
#         article_url = 'https://tengrinews.kz' + article.find('a').get('href')
#         all_articles_dict[article.find('span').text] = article_url
#
#     else:
#         continue
#
# with open('all_articles_dict.json', 'w', encoding='utf-8') as file:
#     json.dump(all_articles_dict, file, indent=4, ensure_ascii=False)

with open('all_articles_dict.json', encoding='utf-8') as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
__id = 0
print(f"Всего итерации: {iteration_count}")

for category_name, category_url in all_categories.items():

    repl = [',', ' ', '-', '"', '!', '?', '.' '/']
    for char in repl:
        if char in category_name:
            category_name = category_name.replace(char, '_')

    req = requests.get(url=category_url, headers=headers)
    src = req.text

    with open(f'data/{__id}_{category_name}.html', 'w', encoding='utf-8') as file:
        file.write(src)
    with open(f'data/{__id}_{category_name}.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    # Собираем текста каждой публикации

    every_publication = soup.find(class_="tn-news-text")
    product_title = soup.find(class_='tn-content-title')

    product_info = []
    if every_publication:
        for publication in every_publication:
            text = every_publication.text
            title = product_title.text

            product_info.append(
                {
                    'Title': title,
                    'Text': text
                }

            )
        with open(f'data/{__id}_{category_name}.txt', 'a', encoding='utf-8') as file:
            file.write(text)
        with open(f"data/{__id}_{category_name}.json", 'a', encoding='utf-8') as file:
            json.dump(product_info, file, indent=4, ensure_ascii=False)

        __id += 1
        print(f"# Итерации {__id}. {category_name} записан...")
        iteration_count = iteration_count - 1
        if iteration_count == 0:
            print("Работа завершена")
            break

        print(f'Осталось итерации: {iteration_count}')
        sleep(random.randrange(2, 4))
    else:
        continue