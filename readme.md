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
- Clear command-line output and helpful error messages
- Unit tests for the crawler, indexer, and search functions

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
|-- tests/
|   |-- test_crawler.py
|   |-- test_indexer.py
|   `-- test_search.py
|-- requirements.txt
|-- readme.md
```

## Requirements

Install the project dependencies with:

```bash
pip install -r requirements.txt
```

The requirements file includes `requests`, `beautifulsoup4`, and `pytest`.

## How to Run

Run the main program from the project root:

```bash
python src/main.py
```

The program will start an interactive command prompt:

```text
Web Crawler Search Tool
Type 'help' to see available commands.
>
```

## Commands

### Build the Index

```text
build
```

This command crawls the target website, saves the page text to `data/pages.json`, builds the inverted index, and saves it to `data/index.json`.

Example output:

```text
Starting crawl...
Crawling: https://quotes.toscrape.com/
Waiting 6 seconds before next request...
...
Saved crawled pages to data/pages.json (10 page(s)).
Built index with 1644 unique word(s).
Saved index to data/index.json.
```

### Load the Index

```text
load
```

This command loads the saved index from `data/index.json`.

If the index file is missing or invalid, the program prints a clear error message.

### Print a Word Entry

```text
print <word>
```

Example:

```text
print life
```

This prints the indexed page and word positions for `life`.

Example output:

```text
Word: life
Found on 10 page(s):
- https://quotes.toscrape.com/
  Positions: [15, 22, 39]
```

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

### Help

```text
help
```

This command prints the list of available commands.

## Example Session

```text
Web Crawler Search Tool
Type 'help' to see available commands.
> build
Starting crawl...
Crawling: https://quotes.toscrape.com/
Waiting 6 seconds before next request...
Crawling: https://quotes.toscrape.com/page/2/
Waiting 6 seconds before next request...
...
Crawling: https://quotes.toscrape.com/page/10/
Saved crawled pages to data/pages.json (10 page(s)).
Built index with 1644 unique word(s).
Saved index to data/index.json.
> load
Index loaded from data/index.json (1644 unique word(s)).
> find life
Pages found for 'life' (10 result(s)):
- https://quotes.toscrape.com/
- https://quotes.toscrape.com/page/10/
- https://quotes.toscrape.com/page/2/
...
> print love
Word: love
Found on 10 page(s):
- https://quotes.toscrape.com/
  Positions: [197, 269]
...
> find good friends
Pages found for 'good friends' (6 result(s)):
- https://quotes.toscrape.com/
- https://quotes.toscrape.com/page/2/
- https://quotes.toscrape.com/page/3/
...
> exit
Goodbye.
```

## Version 3 Features

Version 3 adds:

- Automatic pagination across all quote pages
- A 6 second delay between requests
- `save_pages()` in `crawler.py`
- Saved crawl output in `data/pages.json`
- Cleaner regular-expression tokenisation in `indexer.py`
- Safer command handling for empty `print` and `find` commands

## Current Improvements

This version also includes:

- `requirements.txt` for repeatable dependency installation
- Unit tests in the `tests` folder
- Clearer command output with result counts and formatted page lists
- Error handling for missing or invalid index files
- Error handling when crawling returns no pages
- A protected `main()` entry point so modules can be imported safely by tests

## Data Files

After running `build`, the `data` folder should contain:

```text
data/
|-- pages.json
`-- index.json
```

`pages.json` stores each URL and its extracted text.

`index.json` stores the inverted index. Each word maps to the pages where it appears and the word positions on those pages.

## Running Tests

Run the unit tests from the project root:

```bash
python -m pytest
```

The tests cover:

- Clean tokenisation and index building
- Saving and loading the index
- Single-word and multi-word AND search
- Query punctuation handling
- Clear `print` output
- Crawler pagination and the 6 second wait, using mocked requests
- Saving crawled pages to JSON

## Notes

The crawler handles network errors without crashing. If a request fails, it prints an error message and stops crawling. Search uses AND logic for multi-word queries, so all query words must appear on the same page. Search results are sorted to make the command output and tests stable.
