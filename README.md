# Text Generator

This project is from Jetbrains Academy Python Core track. Level Hard.

## Description

In this project, I used a corpus (a collection of textual data) that contains the entire script of Game of Thrones. The corpus is used to
"train" a probabilistic model that predicts the next word in a chain of words, the generated text resembles 
the style and vocabulary of the source material. The naturalness of the generated text depends on the data. The bigger 
the corpus, the better the results. The corpus used in this project consists of around 300,000 tokens. 
That is not perfect, but it's good enough to get interesting results.

### Functionality
The program prompts the user for a path to file containing corpus. 
If the path is correct, it splits the corpus into individual tokens (separated by space), then it builds the 
model (a Markov model) which consists of trigrams: basically a dictionary with key (head) - a pair of consecutive tokens from
the corpus, and value (tail) - a collections.Counter of the third consecutive token to its frequency (i.e. the  number of times it appears in the corpus
exactly after the previous two consecutive tokens).
After that the program generates 10 random sentences with the following characteristics:
  - always starts with capitalized words ("This is beautiful.", "You are a great programmer!", etc.);
  - doesn't start with a word that ends with a sentence-ending punctuation mark ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
  - always ends with a sentence-ending punctuation mark like ., !, or ?; 
  - is not shorter than 5 tokens.

### Example

The greater-than symbol followed by a space (> ) represents user input.

The output of your program should have the same formatting as shown below.
```text
> corpus.txt
I sent men over the Wall every night.
Kill him! Kill all who understand the law.
They say 1,000 slaves died building the Great Keep at Winterfell.
Queen Margaery. She walked in on Craster's Keep on the Iron Throne.
They say 1,000 slaves died building the Great Keep at Winterfell.
And why is the wheel our queen when she needed me the most.
Dothraki omens. I waited 17 years ago there came a night with no regrets.
Ah, yes. You shall now be held accountable.
Don't cry. It will all be for you.
Never understood why some knights felt the tears freeze on their own.
```