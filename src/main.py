import json

from crawler import crawl_site, save_pages
from indexer import build_index, save_index, load_index
from search import print_word, find_query


def print_help():
    print("Available commands:")
    print("- build          Crawl pages, save data/pages.json, and build data/index.json")
    print("- load           Load data/index.json")
    print("- print <word>   Show pages and positions for one word")
    print("- find <query>   Find pages containing all query words")
    print("- exit / quit    Stop the program")


def main():
    index = {}
    print("Web Crawler Search Tool")
    print("Type 'help' to see available commands.")

    while True:
        cmd = input("> ").strip()

        if cmd == "build":
            print("Starting crawl...")
            pages = crawl_site()

            if not pages:
                print("No pages were crawled. Index was not updated.")
                continue

            save_pages(pages)
            print(f"Saved crawled pages to data/pages.json ({len(pages)} page(s)).")

            index = build_index(pages)
            save_index(index)
            print(f"Built index with {len(index)} unique word(s).")
            print("Saved index to data/index.json.")

        elif cmd == "load":
            try:
                index = load_index()
                print(f"Index loaded from data/index.json ({len(index)} unique word(s)).")
            except FileNotFoundError:
                print("Index file not found. Please run 'build' first.")
            except json.JSONDecodeError:
                print("Index file is not valid JSON. Please run 'build' again.")

        elif cmd == "print":
            print("Please provide a word. Example: print love")

        elif cmd.startswith("print "):
            word = cmd.split(" ", 1)[1].strip()
            if not word:
                print("Please provide a word. Example: print love")
            elif not index:
                print("Index is empty. Please run 'build' or 'load' first.")
            else:
                print_word(index, word)

        elif cmd == "find":
            print("Please provide a search query. Example: find good friends")

        elif cmd.startswith("find "):
            query = cmd.split(" ", 1)[1].strip()
            if not query:
                print("Please provide a search query. Example: find good friends")
            elif not index:
                print("Index is empty. Please run 'build' or 'load' first.")
            else:
                results = find_query(index, query)

                if results:
                    print(f"Pages found for '{query}' ({len(results)} result(s)):")
                    for url in results:
                        print(f"- {url}")
                else:
                    print(f"No pages found for '{query}'.")

        elif cmd == "help":
            print_help()

        elif cmd in ["exit", "quit"]:
            print("Goodbye.")
            break

        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
