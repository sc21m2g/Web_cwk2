import json
import os
import re


def build_index(pages):
    index = {}

    for url, text in pages.items():
        words = re.findall(r"[a-zA-Z0-9']+", text.lower())

        for pos, word in enumerate(words):
            index.setdefault(word, {}).setdefault(url, []).append(pos)

    return index


def save_index(index, filename="data/index.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def load_index(filename="data/index.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
