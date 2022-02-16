from nltk import regexp_tokenize
from collections import Counter
from collections import defaultdict
import regex
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


def last_word_correct(_last_word):
    if not _last_word:
        return False
    last_symbol = _last_word[len(_last_word) - 1]
    return last_symbol in ".!?"


def sentence_length_correct(_sentence):
    _tokens = _sentence.split()
    return len(_tokens) >= 5


def create_sentence(_start, _bigrams):
    sentence = _start
    next_word = ""
    while not sentence_length_correct(sentence) or not last_word_correct(next_word):
        tails = list(_bigrams[_start].keys())
        weights = list(_bigrams[_start].values())
        next_word = random.choices(tails, weights)[0]
        _start = next_word
        sentence += ' ' + next_word
    return sentence


def check_start(start):
    pattern = "[A-Z]"
    first_is_upper_letter = regex.match(pattern, start)
    last_not_punctuation = start[len(start) - 1] not in ".!?"
    return first_is_upper_letter and last_not_punctuation


def handle_input(_bigrams):
    sentence_count = 0
    start = random.choice(list(_bigrams))
    while not check_start(start):
        start = random.choice(list(_bigrams))
    while sentence_count < 10:
        sencente = create_sentence(start, _bigrams)
        print(sencente)
        prev_start = start
        start = random.choice(list(_bigrams))
        while not check_start(start) or start == prev_start:
            start = random.choice(list(_bigrams))
        sentence_count += 1


if __name__ == '__main__':
    tokens = get_tokens_from_file()
    bigrams = get_bigrams_from_tokens(tokens)
    handle_input(bigrams)
