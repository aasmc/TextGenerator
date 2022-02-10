# Text Generator

This project is from Jetbrains Academy Python Core track. Level Hard.

## Description

TBD

## Stage 1

### Objectives

In order to prepare the corpus for use in this project, we need to take the following important steps:

- Open and read the corpus from the provided file corpus.txt. The filename should be specified as user input. Note that
  the file is written in UTF-8 encoding, and the file should be in the same folder as your Python script.
- Break the corpus into individual words. To create a Markov model, we use the simplest form of tokenization: tokens are
  separated by whitespace characters such as spaces, tabulation, and newline characters. Punctuation marks should be
  left untouched since later on, they will play an important role in signaling where a sentence should end.
- Acquire and print the following information about the corpus under the section of the output called Corpus statistics: 
  - the number of all tokens; 
  - the number of all unique tokens, that is, the number of tokens without repetition. Each
      of the above should be in a new line.
- Take an integer as user input and print the token with the corresponding index. Repeat this process until the string
  exit is input. Also, make sure that the input index is actually an integer that falls in the range of the corpus. If
  that is not the case, print an error message and request a new input. Error messages should contain the types of
  errors (Type Error, Index Error, Value Error, etc.). Each token should be printed in a new line.

### Example
The output of the program should look like this. Note that this is just an example: you might get completely different results.
```text
> corpus.txt
Corpus statistics
All tokens: 32434234
Unique tokens: 433242

> 0
What
> 4
They're
> 5
savages.
> 32
like
> 42
ever
> 65
dead
> 256
the
> 532
are
> 756
king,
> 943287563823572346
Index Error. Please input an integer that is in the range of the corpus.
> six
Type Error. Please input an integer.
> -1
North!
> exit
```

## Stage 2
After the training data is acquired and preprocessed, it has to be transformed into a Markov chain model. The first step is to map the connections between tokens in the corpus. For this, we are going to use bigrams.
### Objectives

- Transform the corpus into a collection of bigrams. The results should contain all the possible bigrams from the corpus, which means that:
  - Every token from the corpus should be a head of a bigram with the exception of the last token which cannot become a head since nothing follows it;
  - Every token from the corpus should be a tail of a bigram with the exception of the first token which cannot possibly be the tail of a bigram because nothing precedes it.
- Output the number of all bigrams in the corpus.
- Take an integer as user input and print the bigrams with the corresponding index. Repeat this process until the string exit is input. Also, make sure that the input is actually an integer that falls in the range of the collection of bigrams. If that is not the case, print an error message and request a new input. Error messages should contain the types of errors (Type Error, Value Error, Index Error, etc.). Each bigram should have the format Head: [head] Tail: [tail] and should be printed in a new line.

You should only print the output of the current stage and not the previous one, but like in the previous stage, the name of the file that contains the corpus should be given as user input.
### Example

The greater-than symbol followed by a space (> ) represents user input.

This is what the expected input should look like. Tabs and spaces do not matter during testing, but newlines do.
```text
> corpus.txt
Number of bigrams: 2343554

> 0
Head: What     Tail: do
> 4
Head: They're  Tail: savages.
> 5
Head: savages. Tail: One
> 34
Head: I've     Tail: never
> 42
Head: ever     Tail: in
> 256
Head: the      Tail: lads
> 453
Head: sentence Tail: you
> 2345
Head: don't    Tail: understand
> 3000
Head: can      Tail: protect
> 943287563823572346
Index Error. Please input a value that is not greater than the number of all bigrams.
> six
Type Error. Please input an integer.
> -1
Head: the      Tail: North!
> exit
```