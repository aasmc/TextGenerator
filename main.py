from nltk import regexp_tokenize
from collections import Counter
from collections import defaultdict


def print_tails_for_head(_bigrams, _head):
    tails = (_bigrams[_head]).most_common()
    print(f"Head: {_head}")
    for name in tails:
        print(f"Tail: {name[0]} \tCount: {name[1]}")


def get_tokens_from_file():
    file_name = input()
    pattern = r"[^\s]+"
    _tokens = []
    with open(file_name, "r", encoding="utf-8") as corpus_file:
        for line in corpus_file:
            line_tokens = regexp_tokenize(line, pattern)
            _tokens.extend(line_tokens)
    return _tokens


def get_bigrams_from_tokens(_tokens):
    _bigrams = defaultdict(Counter)
    for i in range(0, len(_tokens) - 1):
        _bigrams[tokens[i]][tokens[i + 1]] += 1
    return _bigrams


def check_input(_bigrams, head_str):
    if head_str not in _bigrams:
        print("Key Error. The requested word is not in the model. Please input another word.")
        return False
    else:
        return True


def handle_input(_bigrams):
    while True:
        head_str = input()
        if head_str == "exit":
            break
        if check_input(_bigrams, head_str):
            print_tails_for_head(_bigrams, head_str)


if __name__ == '__main__':
    tokens = get_tokens_from_file()
    bigrams = get_bigrams_from_tokens(tokens)
    handle_input(bigrams)
