import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from search import find_query


def test_find_single_word():
    index = {
        "life": {
            "page1": [0],
            "page2": [3]
        }
    }

    result = find_query(index, "life")

    assert set(result) == {"page1", "page2"}


def test_find_multi_word_and_query():
    index = {
        "good": {
            "page1": [0],
            "page2": [1]
        },
        "friends": {
            "page1": [2]
        }
    }

    result = find_query(index, "good friends")

    assert result == ["page1"] or set(result) == {"page1"}


def test_find_nonexistent_word():
    index = {
        "life": {
            "page1": [0]
        }
    }

    result = find_query(index, "unknown")

    assert result == []


def test_find_empty_query():
    index = {
        "life": {
            "page1": [0]
        }
    }

    result = find_query(index, "")

    assert result == []