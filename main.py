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


def get_trigrams_from_tokens(_tokens):
    _bigrams = defaultdict(Counter)
    for i in range(0, len(_tokens) - 2):
        key = f"{_tokens[i]} {_tokens[i + 1]}"
        _bigrams[key][_tokens[i + 2]] += 1
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


def create_sentence(_start, _trigrams):
    sentence = _start
    next_word = ""
    while not sentence_length_correct(sentence) or not last_word_correct(next_word):
        tails = list(_trigrams[_start].keys())
        weights = list(_trigrams[_start].values())
        next_word = random.choices(tails, weights)[0]
        prev_word = _start.split()[1]
        _start = f"{prev_word} {next_word}"
        sentence += ' ' + next_word
    return sentence


def check_start(start):
    """Checks whether a given string [start] consists of two words,
    begins with a capital letter, and there're no punctuation marks such as:
    . or ? or ! between the words or at the end of the second word"""
    pattern = r"[A-Z][^\s.!?]* [^\s.!?]+"
    first_is_upper_letter = regex.match(pattern, start)
    return first_is_upper_letter


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
    trigrams = get_trigrams_from_tokens(tokens)
    handle_input(trigrams)
