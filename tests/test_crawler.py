import json
import sys
from pathlib import Path

import requests


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import crawler
from crawler import crawl_site, save_pages


class FakeResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        return None


class FakeSession:
    def __init__(self):
        self.trust_env = True
        self.urls = []

    def get(self, url, timeout):
        self.urls.append((url, timeout))

        if url == "https://quotes.toscrape.com/":
            return FakeResponse(
                "<html><body>First page<li class='next'><a href='/page/2/'>Next</a></li></body></html>"
            )

        if url == "https://quotes.toscrape.com/page/2/":
            return FakeResponse("<html><body>Second page</body></html>")

        raise requests.RequestException("unexpected url")


def test_crawl_site_follows_next_link_and_waits(monkeypatch):
    fake_session = FakeSession()
    sleeps = []

    monkeypatch.setattr(crawler.requests, "Session", lambda: fake_session)
    monkeypatch.setattr(crawler.time, "sleep", lambda seconds: sleeps.append(seconds))

    pages = crawl_site()

    assert list(pages.keys()) == [
        "https://quotes.toscrape.com/",
        "https://quotes.toscrape.com/page/2/",
    ]
    assert "First page" in pages["https://quotes.toscrape.com/"]
    assert "Second page" in pages["https://quotes.toscrape.com/page/2/"]
    assert fake_session.trust_env is False
    assert sleeps == [6]


def test_save_pages_creates_json_file():
    pages = {
        "https://example.com/": "Example text"
    }
    filename = Path(__file__).parent / "_tmp" / "pages.json"

    filename.parent.mkdir(exist_ok=True)
    if filename.exists():
        filename.unlink()

    save_pages(pages, str(filename))

    assert json.loads(filename.read_text(encoding="utf-8")) == pages

    filename.unlink()
