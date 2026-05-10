from crawler import crawl_site
from indexer import build_index, save_index, load_index
from search import print_word, find_query

index = {}

while True:
    cmd = input("> ").strip()

    if cmd == "build":
        pages = crawl_site()
        index = build_index(pages)
        save_index(index)
        print("Index built and saved.")

    elif cmd == "load":
        index = load_index()
        print("Index loaded.")

    elif cmd.startswith("print "):
        word = cmd.split(" ", 1)[1]
        print_word(index, word)

    elif cmd.startswith("find "):
        query = cmd.split(" ", 1)[1]
        results = find_query(index, query)

        if results:
            print("Pages found:")
            for url in results:
                print(url)
        else:
            print("No pages found.")

    elif cmd in ["exit", "quit"]:
        break

    else:
        print("Unknown command.")
