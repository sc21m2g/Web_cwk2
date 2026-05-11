import re


def print_word(index, word):
    word = word.lower().strip()

    if not word:
        print("Please provide a word to print.")
        return

    if word in index:
        pages = index[word]
        print(f"Word: {word}")
        print(f"Found on {len(pages)} page(s):")
        for url in sorted(pages):
            positions = pages[url]
            print(f"- {url}")
            print(f"  Positions: {positions}")
    else:
        print(f"Word not found: {word}")


def find_query(index, query):
    words = re.findall(r"[a-zA-Z0-9']+", query.lower())

    if not words:
        return []

    result_pages = None

    for word in words:
        if word not in index:
            return []

        pages = set(index[word].keys())

        if result_pages is None:
            result_pages = pages
        else:
            result_pages = result_pages.intersection(pages)

    return sorted(result_pages)
