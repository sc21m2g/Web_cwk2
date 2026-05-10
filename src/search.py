def print_word(index, word):
    word = word.lower()
    if word in index:
        print(index[word])
    else:
        print("Word not found")

def find_query(index, query):
    words = query.lower().split()

    if not words:
        print("Empty query")
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

    return list(result_pages)
