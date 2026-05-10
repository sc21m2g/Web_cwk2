from crawler import crawl_site
from indexer import build_index, save_index
from search import print_word
import json

index = {}

while True:
    cmd = input("> ").strip()
    if cmd == "build":
        pages = crawl_site()
        index = build_index(pages)
        save_index(index)
        print("Index built and saved.")
    elif cmd.startswith("print "):
        word = cmd.split(" ",1)[1]
        print_word(index, word)
    elif cmd in ["exit", "quit"]:
        break