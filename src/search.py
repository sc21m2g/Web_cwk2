def print_word(index, word):
    word = word.lower()
    if word in index:
        print(index[word])
    else:
        print("Word not found")