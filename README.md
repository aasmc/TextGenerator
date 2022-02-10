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
  - — the number of all tokens; 
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