import json

def build_index(pages):
    index = {}
    for url, text in pages.items():
        words = text.lower().split()
        for pos, word in enumerate(words):
            index.setdefault(word, {}).setdefault(url, []).append(pos)
    return index

def save_index(index, filename="data/index.json"):
    with open(filename, "w") as f:
        json.dump(index, f)