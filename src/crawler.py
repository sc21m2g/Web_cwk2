import json
import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def crawl_site(base_url="https://quotes.toscrape.com/"):
    pages = {}
    current_url = base_url

    session = requests.Session()
    session.trust_env = False

    while current_url:
        try:
            print(f"Crawling: {current_url}")
            response = session.get(current_url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {current_url}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        pages[current_url] = text

        next_link = soup.select_one("li.next > a")

        if next_link:
            current_url = urljoin(base_url, next_link["href"])
            print("Waiting 6 seconds before next request...")
            time.sleep(6)
        else:
            current_url = None

    return pages


def save_pages(pages, filename="data/pages.json"):
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    pages = crawl_site()
    save_pages(pages)
    print(f"Crawled and saved {len(pages)} pages.")
