# Advanced User Input

In this exercise, we need to create a module that passed the tests of lexicon_tests.py file.

What given to do in this exercise:
1. List of allowed words (aka lexicon):
    - directions words: north, east, west, south, up, down, left, right, back
    - verbs: go, stop, kill, eat
    - stops: the, in, of, from, at, it
    - nouns: door, bear, princess, cabinet
    - number: any string 0 through 9 character
2. for break sentence `str.split()`:
    ```py
    words = sentence.split()
    ```
3. Lexicon tuple, tuple is an immutable list notice by ():
    ```
    first_word = ('direction', 'north')
    second_word = ('direction', 'south')
    sentence = [first_word, second_word]
    ```
4. Exception and Number:
    ```py
    def convert_number(s):
        try:
            return int(s)
        except:
            return None
    ```

This above help in completing this exercise. Check [lexicon_tests.py](./exercise/tests/lexicon_tests.py) file.

This exercise done in similar way as skeleton exercise.

## Exercise

1. Make lexicon.py in ex48 dir.
    ```py
    allowd_words = {
            'direction' : ['north', 'south', 'east', 'west',
                'down', 'up', 'left', 'right', 'back'],
            'verb' : ['go', 'stop', 'kill', 'eat'],
            'stop' : ['the', 'in', 'of', 'from', 'at', 'it'],
            'noun' : ['door', 'bear', 'princess', 'cabinet'],
            }

    def breakup_sentence(string):
        "Breaking Up a sentence and return list"
        return string.split()

    def check(word):
        "Check of word"
        for token in allowd_words:
            if word in allowd_words[token]:
                return (token, word)
        return ('error', word)

    def convert_number(word):
        "Convert num string in integer"
        try:
            return int(word)
        except ValueError:
            return word

    def result(lst):
        "Return result"
        res = []
        for word in lst:
            num = convert_number(word)
            if word != num:
                res.append(('number', word))
                continue
            res.append(check(word))
        return res

    def scan(string):
        "Scan input and return result"
        words_list = breakup_sentence(string)
        return result(words_list) 
    ```
2. This is test file.
    ```py
    from ex48 import lexicon

    def test_dir():
        assert lexicon.scan("north") == [('direction', 'north')]
        result = lexicon.scan("north south east")
        assert result == [('direction', 'north'),
                ('direction', 'south'),
                ('direction', 'east')]

    def test_verbs():
        assert lexicon.scan("go") == [('verb', 'go')]
        result = lexicon.scan("go kill eat")
        assert result == [('verb', 'go'),
                ('verb', 'kill'),
                ('verb', 'eat')]

    def test_stops():
        assert lexicon.scan("the") == [('stop', 'the')]
        result = lexicon.scan("the in of")
        assert result == [('stop', 'the'),
                ('stop', 'in'),
                ('stop', 'of')]

    def test_nouns():
        assert lexicon.scan("bear") == [('noun', 'bear')]
        result = lexicon.scan("bear princess")
        assert result == [('noun', 'bear'),
                ('noun', 'princess')]

    def test_numbers():
        assert lexicon.scan("1234") == [('number', '1234')]
        result = lexicon.scan("3 91234")
        assert result == [('number', '3'),
                ('number', '91234')]

    def test_errors():
        assert lexicon.scan("ASDFADFASDF") == [('error', 'ASDFADFASDF')]
        result = lexicon.scan("bear IAS princess")
        assert result == [('noun', 'bear'),
                ('error', 'IAS'),
                ('noun', 'princess')]
    ```
3. Check all test run successfully.
    ```sh
    $ pytest tests/lexicon_tests.py 
    ========================== test session starts ===========================
    platform linux -- Python 3.12.8, pytest-8.4.0, pluggy-1.6.0
    rootdir: /home/nat/Desktop/repos/learn-python-the-hard-way/Exercises/exercise-48-advanced-user-input/exercise
    collected 6 items                                                        

    tests/lexicon_tests.py ......                                      [100%]

    =========================== 6 passed in 0.01s ============================
    ```
