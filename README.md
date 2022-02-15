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

## Stage 3

### Theory

We already mentioned Markov chains a few times. A Markov chain is a statistical model in which the probability of each event depends on the previous event. It can be described as a set of states and transitions between them. Each transition has a probability that is determined by some kind of statistical data. In this project, a state corresponds to a token, and each transition represents going from one word of a sentence to another. The probability of transitions is calculated from the bigrams we collected in the previous stage. The basic idea of this project is that from a dictionary we can create a model that will consider all the possible transitions from one word to another and choose the most probable one based on the previous word.

### Description
This is the final step where we will work on creating a Markov chain model. We will use the data prepared in the first two stages and transform it into a model. This model will contain probabilistic information that will tell us what the next word in a chain might be.

We already have a list of all bigrams from the corpus. As we discussed earlier, this can already be used to make some naive predictions. There is a problem, though: right now our data contains a lot of repetition. As we have seen at the first stage, the total number of tokens is almost 10 times greater than the number of unique tokens. This ratio must be about the same in the list of bigrams. Some bigrams might be very common, others — relatively rare. At the moment, we have no way of telling which are which.

To resolve this problem, we will make a simplified version of a Markov chain model.

### Objectives
- The data should be reorganized in such a way that every head is repeated only once, and all the possible tails can be directly accessed by querying that head. For example: head — good, tails — night, bye, bye, night, to, to, bye, boy. As you can see, there are still some repetitions among the tails.
- Instead of repeating tails every time they occur, each tail should appear only once and the number of repetitions should be stored as an integer. For example, the previous example should look like this: head — good, tails — night: 2, bye: 3, to: 2, boy: 1. You can see that the data is more readable after this transformation!
- Besides creating the model, we should also check that it works correctly. To test it, let's take a string as user input and print all the possible tails and their corresponding counts. If the model does not contain the specified head print the following error message Key Error. The requested word is not in the model. Please input another word. and ask for another until it is valid. Repeat until the string exit is input.


You should only print the output of the current stage and not the previous one, but like in the previous stage, the name of the file that contains the corpus should be given as user input.

### Example

The greater-than symbol followed by a space (> ) represents user input.

The output of the program should look something like this. The number of tabs and spaces does not matter, but newline characters do.
```text
> corpus.txt
> Night
Head: Night
Tail: King    Count: 17
Tail: gathers Count: 9
Tail: King's  Count: 4
Tail: is      Count: 2

> Jon
Head: Jon
Tail: Snow    Count: 36
Tail: Snow.   Count: 29
Tail: Arryn   Count: 14
Tail: said    Count: 10
Tail: often   Count: 6
Tail: knows   Count: 5
Tail: left    Count: 5

> Northampton
Head: Northampton
Key Error. The requested word is not in the model. Please input another word.

> King
Head: King
Tail: in      Count: 76
Tail: Robert  Count: 29
Tail: of      Count: 24
Tail: Joffrey Count: 20
Tail: Tommen  Count: 6
Tail: Stannis Count: 5
Tail: Robb    Count: 5

> exit
```

## Stage 4
### Theory

We suggest using the method random.choices() to select the most probable tail from the list of possible tails based on the corresponding repetition counts. This method is similar to random.choice() with the exception that it also considers user-specified weights during the process. The method takes four arguments: population, weights, cum_weights, and k. For this project, we only care about the first two arguments: population, which is a list of elements to choose from, and weights, which is a list of relative weights that correspond to the elements of the population. Since the other two arguments have sensible default values, we don't necessarily have to specify them.
Description

We have our model, fantastic! What's next? Well, the model can already be used to predict the next word in a chain by feeding it any head (of a bigram) from the corpus and retrieving the most probable tail from the corresponding entry. But how do we start the chain, what should be the first word?

Of course, we could choose a word manually, but this is an error-prone solution because we might take a word that is not in the corpus. A better way to start is to choose a random word from the corpus and feed it to the model so that it predicts the next word.
After the next word is acquired, it should be used to predict the following word, and so on, thus continuing the chain.

Objectives

- Choose a random word from the corpus that will serve as the first word of the chain.
- The second word should be predicted by looking up the first word of the chain in the model and choosing the most probable next word from the set of possible follow-ups. Right now, an entry contains all the possible tails that might follow the selected head along with their corresponding repetition counts. Using the repetition counts, you will be able to choose the most probable option.
- The second step should be repeated until the length of the chain is 10 words, but this time, the current last word of the chain should be used to look up another probable word to continue the sentence.

Using the algorithm described above, generate chains consisting of 10 tokens, join the resulting tokens together, and print them as a pseudo-sentence. Keep in mind that a pseudo-sentence can consist of multiple actual sentences, so having punctuation marks inside pseudo-sentences is completely valid.

Generate and print 10 sentences like that. Keep in mind that every generated pseudo-sentence should be on a new line.

You should only print the output of the current stage and not the previous one. The name of the file that contains the corpus should be given as a command line input.

### Example

The greater-than symbol followed by a space (> ) represents user input.

The output of your program should have the same formatting style.

```text
> corpus.txt
so I saw him grow up against me halfway out
Queen of the night ashore for-- water. The Lannister song?
honor for all reading about me? Can't. Someone appears to
she would be easier than I sliced me, My atonement?
your days. Robert's return. A mountain of Casterly Rock. Has
much do me roar! For the King in the Kingslayer?
the side my pride. Don't lose. Have you were you
for you out there will take it You don't know.
she crucified the rest of them. The Boltons, the Watch
father Tywin sent here in their minds aren't they lick
```

## Stage 5
### Description

As you can see, the algorithm is now capable of generating pseudo-random text based on Markov chains. The problem is that the resulting text does not resemble real sentences at all. First, the resulting text is always ten tokens long. Second, it does not always start with capital letters. Third, it usually does not even end with correct punctuation such as periods, exclamation marks, or question marks.

Luckily, by identifying the problem, a good programmer can always find ways to resolve it.
- Make the algorithm more realistic by generating pseudo-sentences instead of just random text. The sentences that are being generated should:
  - always start with capitalized words ("This is beautiful.", "You are a great programmer!", etc.);
  - not start with a word that ends with a sentence-ending punctuation mark ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
  - always end with a sentence-ending punctuation mark like ., !, or ?; 
  - should not be shorter than 5 tokens.
- Generate and print exactly 10 pseudo-sentences that meet these criteria. A pseudo-sentence should end when the first sentence-ending punctuation mark is encountered after the minimal sentence length (5 tokens) is reached.

Note that every generated pseudo-sentence should be on a new line.

You should only print the output of the current stage and not the previous one. The name of the file that contains the corpus should be given as user input.

### Example

The greater-than symbol followed by a space (> ) represents user input.

The output of your program should look something like this but with different sentences.
```text
> corpus.txt
Ned Stark can still hold my head off, too.
Just look at us. It's still remember seeing each of Yunkai have had nothing anymore.
Braavos never attacks the Starks?
I don't think it's true.
I'm a captain. Of course he has a woman to protect us.
Trust me about them? He smells of the northern sons.
They have sold armor. I've taken your captors is how goes off our grasp.
I realized peace while my years has a Lannister.
Did you like the North more than your life?
With my brothers and the dawn I serve in irons.
```