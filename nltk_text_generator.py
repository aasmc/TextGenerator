from nltk.util import ngrams

bigrams = list(ngrams(open(input(), "r", encoding="utf-8").read().split(), 2))
print("Number of bigrams:", len(bigrams))
while True:
    entry = input()
    if entry == "exit":
        break
    try:
        print("Head:", bigrams[int(entry)][0] + "\t", "Tail:", bigrams[int(entry)][1])
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
    except (TypeError, ValueError):
        print("Type Error. Please input an integer.")