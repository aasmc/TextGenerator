from nltk import regexp_tokenize
from collections import Counter
from collections import defaultdict
import random


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


def print_tails_for_head(_bigrams, _head):
    tails = (_bigrams[_head]).most_common()
    print(f"Head: {_head}")
    for name in tails:
        print(f"Tail: {name[0]} \tCount: {name[1]}")


def create_sentence(_start, _bigrams):
    sentence = _start
    next_word = ""
    for i in range(9):
        tails = list(_bigrams[_start].keys())
        weights = list(_bigrams[_start].values())
        next_word = random.choices(tails, weights)[0]
        _start = next_word
        sentence += ' ' + next_word
    return sentence, next_word


def handle_input(_bigrams):
    sentence_count = 0
    start = random.choice(list(_bigrams))
    while sentence_count < 10:
        sencente, last = create_sentence(start, _bigrams)
        print(sencente)
        start = _bigrams[last].most_common()[0][0]
        sentence_count += 1


if __name__ == '__main__':
    tokens = get_tokens_from_file()
    bigrams = get_bigrams_from_tokens(tokens)
    handle_input(bigrams)
