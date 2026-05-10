# Web Crawler and Search Index

Target website:

https://quotes.toscrape.com/

This project is a small Python crawler and search tool. It crawls text from the target website, builds an inverted index, saves the index as JSON, and supports simple word search commands from the terminal.

## Features

- Crawl the target website homepage
- Extract page text with BeautifulSoup
- Build a basic inverted index
- Save the index to `data/index.json`
- Load a previously saved index
- Print index information for a single word
- Find pages that contain one or more query words

## Project Structure

```text
cwk2/
|-- data/
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


## Version 2 Features

Version 2 adds:

- `load_index()` in `indexer.py`
- Better JSON saving with UTF-8 encoding and indentation
- `find_query()` in `search.py`
- `load` command in `main.py`
- `find` command in `main.py`
- Support for multi-word AND queries

## Notes

The current crawler only crawls the homepage of the target website. The index is simple and uses whitespace-based tokenisation, so punctuation may remain attached to some words.
