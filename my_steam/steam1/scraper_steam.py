import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time

url = 'https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&snr' \
      '=1_7_7_2300_7&specials=1&supportedlang=english&infinite=1'


def totalresults(url):
    r = requests.get(url)
    data = dict(r.json())
    totalresults = data['total_count']
    return int(totalresults)


def get_data(url):
    r = requests.get(url)
    data = dict(r.json())
    return data['results_html']


def parse(data):
    gameslist = []
    soup = BeautifulSoup(data, 'html.parser')
    games = soup.find_all('a')
    for game in games:
        title = game.find('span', {'class': 'title'}).text
        price_container = game.find('div', {'class': 'discount_original_price'})

        if price_container:
            price = price_container.text
            try:
                disc_price = game.find('div', {'class': 'discount_final_price'}).text
            except:
                disc_price = price
        else:
            price = "None"
            disc_price = "None"
            print(f'No price available for: {title}')  # Выводим информацию о том, что у игры нет цены

        mygame = {
            'title': title,
            'price': price,
            'disc_price': disc_price
        }
        gameslist.append(mygame)
    return gameslist


def output(results):
    games_df = pd.concat([pd.DataFrame(g) for g in results])
    csv_path = 'media/games_list2.csv'
    games_df.to_csv(csv_path, index=False)
    print(f'Fin. Saved to CSV: {csv_path}')
    print(games_df.head())
    return


results = []
# for x in range(0, totalresults(url), 50):
for x in range(0, 400, 50):
    data = get_data(
        f'https://store.steampowered.com/search/results/?query&start={x}&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&supportedlang=english&infinite=1')
    results.append(parse(data))
    print('Results Scraped: ', x)
    time.sleep(1.5)



output(results)
