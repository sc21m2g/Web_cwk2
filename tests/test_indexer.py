import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from indexer import build_index


def test_build_index_single_page():
    pages = {
        "page1": "Life is good. Life is beautiful."
    }

    index = build_index(pages)

    assert "life" in index
    assert "good" in index
    assert "beautiful" in index
    assert index["life"]["page1"] == [0, 3]


def test_build_index_case_insensitive():
    pages = {
        "page1": "Good good GOOD"
    }

    index = build_index(pages)

    assert "good" in index
    assert index["good"]["page1"] == [0, 1, 2]


def test_build_index_multiple_pages():
    pages = {
        "page1": "hello world",
        "page2": "hello python"
    }

    index = build_index(pages)

    assert set(index["hello"].keys()) == {"page1", "page2"}
    assert index["world"]["page1"] == [1]
    assert index["python"]["page2"] == [1]