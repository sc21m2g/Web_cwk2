# Web Crawler and Search Index

Target website:

https://quotes.toscrape.com/

This project is a small Python crawler and search tool. It crawls all quote pages from the target website, saves the page text, builds an inverted index, and supports simple word search commands from the terminal.

## Features

- Crawl all pages on the target website by following the `Next` link
- Use a 6 second politeness window between page requests
- Extract page text with BeautifulSoup
- Save crawled page text to `data/pages.json`
- Build a basic inverted index with cleaner regular-expression tokenisation
- Save the index to `data/index.json`
- Load a previously saved index
- Print index information for a single word
- Find pages that contain one or more query words

## Project Structure

```text
cwk2/
|-- data/
|   |-- pages.json
|   `-- index.json
|-- src/
|   |-- crawler.py
|   |-- indexer.py
|   |-- main.py
|   `-- search.py
|-- readme.md
```

## Requirements

The project uses Python and the following packages:

- `requests`
- `beautifulsoup4`

Install them with:

```bash
pip install requests beautifulsoup4
```

## How to Run

Run the main program from the project root:

```bash
python src/main.py
```

The program will start an interactive command prompt:

```text
>
```

## Commands

### Build the Index

```text
build
```

This command crawls the target website, builds the inverted index, and saves it to `data/index.json`.
It also saves the crawled page text to `data/pages.json`.

### Load the Index

```text
load
```

This command loads the saved index from `data/index.json`.

### Print a Word Entry

```text
print <word>
```

Example:

```text
print life
```

This prints the indexed page and word positions for `life`.

### Find Pages

```text
find <query>
```

Examples:

```text
find life
find good friends
```

For a single word, the command returns pages containing that word.

For multiple words, the command uses AND search. This means all query words must appear on the same page.

### Exit

```text
exit
quit
```

Either command stops the program.

## Example Session

```text
> build
Crawling: https://quotes.toscrape.com/
Waiting 6 seconds before next request...
Crawling: https://quotes.toscrape.com/page/2/
Waiting 6 seconds before next request...
...
Crawling: https://quotes.toscrape.com/page/10/
Pages crawled and saved: 10 pages.
Index built and saved.
> load
Index loaded.
> find life
Pages found:
https://quotes.toscrape.com/
https://quotes.toscrape.com/page/5/
https://quotes.toscrape.com/page/8/
...
> print love
{'https://quotes.toscrape.com/': [197, 269], ...}
> find good friends
Pages found:
https://quotes.toscrape.com/
https://quotes.toscrape.com/page/7/
https://quotes.toscrape.com/page/2/
...
> exit
```

## Version 3 Features

Version 3 adds:

- Automatic pagination across all quote pages
- A 6 second delay between requests
- `save_pages()` in `crawler.py`
- Saved crawl output in `data/pages.json`
- Cleaner regular-expression tokenisation in `indexer.py`
- Safer command handling for empty `print` and `find` commands

## Data Files

After running `build`, the `data` folder should contain:

```text
data/
|-- pages.json
`-- index.json
```

`pages.json` stores each URL and its extracted text.

`index.json` stores the inverted index. Each word maps to the pages where it appears and the word positions on those pages.

## Notes

The crawler handles network errors without crashing. If a request fails, it prints an error message and stops crawling. Search uses AND logic for multi-word queries, so all query words must appear on the same page.
