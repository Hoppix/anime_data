import os
import json
from bs4 import BeautifulSoup
import requests


ROOT_URL = "https://myanimelist.net/anime/"
MAX_ID_VALUE = 50000
START_ID = 1
PERSIST=True

def scrape():
    print(f"Scraping {ROOT_URL}")

    for id in range(START_ID, MAX_ID_VALUE):
        data = scrape_by_id(id)

        if PERSIST:
            save_anime_data(id, data, "data")


def scrape_by_id(id):
    
    request_url = f"{ROOT_URL}{id}"
    print(f"Scraping for id: {request_url}")
    page = requests.get(request_url)

    if page.status_code == 200:
        content = page.content
        DOMdocument = BeautifulSoup(content, 'html.parser')

        divs = DOMdocument.find_all("div", {"class": "spaceit_pad"})
        data = {
            "title": "",
            "japanese_title": "",
            "score": 7.2,
            "score_count": 0,
            "ranked": "",
            "popularity": "",
            "favorites": "",
            "airing_type": "TV",
            "episode_count": 0,
            "status": "currently airing",
            "aired": "",
            "premiered": "",
            "producers": "",
            "licensors": "",
            "studios": "",
            "source": "",
            "genres": [],
            "theme": "",
            "duration": "",
            "rating": ""
        }
        print(json.dumps(DOMdocument,indent=4, default=str))
        return data
    else:
        print("Skipping due to non 200 response code")


def save_anime_data(id, data, path=str):
    print(f"Persisting anime_{id}")
    json.dump(data, open(f"{path}/anime_{id}.json", "w+"),indent=4)


if __name__ == "__main__":
    scrape()