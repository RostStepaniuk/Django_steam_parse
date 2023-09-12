import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

STEAM_URL = 'https://store.steampowered.com/search/results/?query&start={}&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_2300_7&specials=1&supportedlang=english&infinite=1'
CSV_PATH = 'media/games_list2.csv'


def total_results(url):
    r = requests.get(url)
    data = dict(r.json())
    total_results = data['total_count']
    return int(total_results)


def get_data(url):
    r = requests.get(url)
    data = dict(r.json())
    return data['results_html']


def parse(data):
    games_list = []
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
            print(f'No price available for: {title}')

        my_game = {
            'title': title,
            'price': price,
            'disc_price': disc_price
        }
        games_list.append(my_game)
    return games_list


def scrape_steam_data():
    results = []
    # for x in range(0, total_results(STEAM_URL.format(0)), 50):
    for x in range(0, 50, 50):
        data = get_data(STEAM_URL.format(x))
        games_data = parse(data)
        results.append(parse(data))
        # print('Results Scraped:', x)
        # print('Games:', games_data)  # Добавьте эту строку для отладки
        time.sleep(1.5)

    return results


def save_to_csv(results):
    games_df = pd.concat([pd.DataFrame(g) for g in results])
    games_df.to_csv(CSV_PATH, index=False)
    print(f'Finished. Saved to CSV: {CSV_PATH}')
    print(games_df.head())


if __name__ == "__main__":
    scraped_data = scrape_steam_data()
    save_to_csv(scraped_data)

