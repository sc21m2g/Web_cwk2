from crawler import crawl_site, save_pages
from indexer import build_index, save_index, load_index
from search import print_word, find_query

index = {}

while True:
    cmd = input("> ").strip()

    if cmd == "build":
        pages = crawl_site()
        save_pages(pages)

        index = build_index(pages)
        save_index(index)

        print(f"Pages crawled and saved: {len(pages)} pages.")
        print("Index built and saved.")

    elif cmd == "load":
        try:
            index = load_index()
            print("Index loaded.")
        except FileNotFoundError:
            print("Index file not found. Please run build first.")

    elif cmd == "print":
        print("Please provide a word to print.")

    elif cmd.startswith("print "):
        word = cmd.split(" ", 1)[1].strip()
        if word:
            print_word(index, word)
        else:
            print("Please provide a word to print.")

    elif cmd == "find":
        print("Please provide a search query.")

    elif cmd.startswith("find "):
        query = cmd.split(" ", 1)[1].strip()
        if query:
            results = find_query(index, query)

            if results:
                print("Pages found:")
                for url in results:
                    print(url)
            else:
                print("No pages found.")
        else:
            print("Please provide a search query.")

    elif cmd in ["exit", "quit"]:
        break

    else:
        print("Unknown command.")
