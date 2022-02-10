from nltk import regexp_tokenize


def get_tokens_from_file():
    file_name = input()
    pattern = r"[^\s]+"
    _tokens = []
    with open(file_name, "r", encoding="utf-8") as corpus_file:
        for line in corpus_file:
            line_tokens = regexp_tokenize(line, pattern)
            _tokens.extend(line_tokens)
    _unique_tokens = set(_tokens)
    return _tokens, _unique_tokens


def process_tokens(_tokens, _unique_tokens):
    print("Corpus statistics")
    print(f"All tokens: {len(_tokens)}")
    print(f"Unique tokens: {len(_unique_tokens)}\n")


def check_input(tokens_len, index_str):
    try:
        index = int(index_str)
        if 0 <= abs(index) < tokens_len:
            return True
        else:
            print("Index Error. Please input an integer that is in the range of the corpus.")
            return False
    except ValueError:
        print("Type Error. Please input an integer.")
        return False


def handle_input(_tokens):
    while True:
        index_str = input()
        if index_str == "exit":
            break
        if check_input(len(_tokens), index_str):
            print(_tokens[int(index_str)])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tokens, unique_tokens = get_tokens_from_file()
    process_tokens(tokens, unique_tokens)
    handle_input(tokens)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
