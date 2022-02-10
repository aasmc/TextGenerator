from nltk import regexp_tokenize


class Bigram:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        result = f"Head: {self.head}  Tail:"
        if self.tail is not None:
            result = f"{result} {self.tail}"
        return result


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
    _bigrams = []
    for i in range(0, len(_tokens) - 1):
        _bigrams.append(Bigram(_tokens[i], _tokens[i + 1]))
    return _bigrams


def process_bigrams(_bigrams):
    print(f"Number of bigrams: {len(_bigrams)}\n")


def check_input(bigrams_len, index_str):
    try:
        index = int(index_str)
        if 0 <= abs(index) < bigrams_len:
            return True
        else:
            print("Index Error. Please input an integer that is in the range of the corpus.")
            return False
    except ValueError:
        print("Type Error. Please input an integer.")
        return False


def handle_input(_bigrams):
    while True:
        index_str = input()
        if index_str == "exit":
            break
        if check_input(len(_bigrams), index_str):
            print(_bigrams[int(index_str)])


if __name__ == '__main__':
    tokens = get_tokens_from_file()
    bigrams = get_bigrams_from_tokens(tokens)
    process_bigrams(bigrams)
    handle_input(bigrams)
