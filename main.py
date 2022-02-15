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
    word_count = 1
    sentence = f"{_start }"
    tails = _bigrams[_start]
    most_common = tails.most_common()
    next_word = most_common[0][0]
    while word_count < 10:
        sentence = f"{sentence} {next_word}"
        tails = _bigrams[next_word]
        most_common = tails.most_common()
        if len(most_common) == 0:
            continue
        if word_count != 9:
            next_word = most_common[0][0]
        word_count += 1
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
