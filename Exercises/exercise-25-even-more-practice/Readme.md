# Even more practice

This time is about function and return but use ex25.py file as an import for python interpreter.

## Exercise

1. Create an ex25.py and write following code:
```py
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_words(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_words(words)
```
2. Start python interpreter, `python` and do following (I made a interpreter-script.py with few changes):
    ```py
    import ex25
    sentence = "All good things come to those who wait."
    words = ex25.break_words(sentence)
    words
    sorted_words = ex25.sort_words(words)
    sorted_words
    ex25.print_first_word(words)
    ex25.print_last_word(words)
    words
    ex25.print_first_word(sorted_words)
    ex25.print_last_word(sorted_words)
    sorted_words
    sorted_words = ex25.sort_sentence(sentence)
    sorted_words
    ex25.print_first_and_last(sentence)
    ex25.print_first_and_last_sorted(sentence)
    ```
    Output:
    ```
    ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
    ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
    All
    wait.
    ['good', 'things', 'come', 'to', 'those', 'who']
    All
    who
    ['come', 'good', 'things', 'those', 'to', 'wait.']
    ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
    All
    wait.
    All
    who
    ```

## Noted

1. Now all function of ex25, start *python interpreter*, then:
    ```py
    >>> import ex25
    >>> help(ex25) # show all possible function.
    ```
2. `import filename` only work if both files present in same directory.