import requests
from bs4 import BeautifulSoup

def crawl_site(base_url="https://quotes.toscrape.com/"):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    return {base_url: text}

if __name__ == "__main__":
    pages = crawl_site()
    print(pages)