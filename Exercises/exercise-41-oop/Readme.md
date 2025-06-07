# Speak Object Oriented

Words that use in Object Oriented.

Word Drills:

|words|Description|
|:---:|:---|
|**class**|Tell python to make a new type of thing.|
|**object**|Two meaning: the most basic type of thing, and any instance of some thing|
|**instance**|What you get when you tell python to create a class|
|**def**|define a function inside a class|
|**self**|Inside the function in a class, self is a variable for the instance/object being accessed|
|**inheritance**|The concept that one class can inherit traits from another class|
|**composition**|The concept that a class an be composed of other classes as parts|
|**attribute**|A property classes have that are from composition and are usually variable|
|**is-a**|A phrase to say that something inherits from another, as in a "salmon" is-a "fish"|
|**has-a**|A phrase to say that something is composed of other things or has a trait, as in a "salmon" has-a "mouth"|

Phrase Drills"

|Python code snippets|Way to say|
|:---|:---|
|class X(Y)|Make a class named X that is-a Y|
|class X(object): def __init__(self, J)|class X has-a __init__ that takes self and J parameters|
|class X(object): def M(self, J)|class X has-a function named M that takes self and J parameters|
|foo = X()|Set foo to an instance of class X|
|foo.M(J)|From foo, get the M function and call it with parameters self, J|
|foo.K = Q|From foo, get the K attribute, and set it to Q|

## Exercise

1. Create an ex41.py and write following:
    ```py
    import random
    from urllib.request import urlopen
    import sys

    WORD_URL = "https://learncodethehardway.org/words.txt"
    WORDS = []

    PHRASES = {
            "class %%%(%%%):":
                "Make a class named %%% that is-a %%%.",
            "class %%%(object):\n\tdef __init__(self, ***)":
                "class %%% has-a __init__ that takes self and *** params.",
            "class %%%(object):\n\tdef ***(self, @@@)":
                "class %%% has-a function *** that takes self and @@@ params.",
            "*** = %%%()":
                "Set *** to an instance of class %%%.",
            "***.***(@@@)":
                "From *** get the *** function, call it with params self, @@@.",
            "***.*** = '***'":
                "From *** get the *** attribute and set it to '***'."
            }

    # do they want to drill phrases first
    if len(sys.argv) == 2 and sys.argv[1] == "english":
        PHRASE_FIRST = True
    else:
        PHRASE_FIRST = False

    # load up the words from the website
    for word in urlopen(WORD_URL).readlines():
        WORDS.append(str(word.strip(), encoding="utf-8"))

    def convert(snippet, phrase):
        class_names  = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
        other_names = random.sample(WORDS, snippet.count("***"))
        results, param_names = [], []

        for i in range(0, snippet.count("@@@")):
            param_count = random.randint(1,3)
            param_names.append(', '.join(
                random.sample(WORDS, param_count)))

        for sentence in snippet, phrase:
            result = sentence[:]

            # fake class names
            for word in class_names:
                result = result.replace("%%%", word, 1)

            # fake other names
            for word in other_names:
                result = result.replace("***", word, 1)

            # fake parameter lists
            for word in param_names:
                result = result.replace("@@@", word, 1)

            results.append(result)

        return results

    # Keep going until they hit CTRL-D
    try:
        while True:
            snippets = list(PHRASES.keys())
            random.shuffle(snippets)

            for snippet in snippets:
                phrase = PHRASES[snippet]
                ques, ans  = convert(snippet, phrase)
                if PHRASE_FIRST:
                    ques, ans = ans, ques

                print(ques)

                input("> ")
                print(f"ANSWER: {ans}\n\n")
    except EOFError:
        print("\nBye")
    ```
2. Run script
    ```
    $ python ex41.py english
    Make a class named Change that is-a Driving.
    > class Change(Driving):
    ANSWER: class Change(Driving):


    class Cracker has-a function bat that takes self and collar, cork params.
    > class Cracker(): def bat(self, collar, cork)
    ANSWER: class Cracker(object):
    	def bat(self, collar, cork)


    class Color has-a __init__ that takes self and copper params.
    > class Color(object): def __init__(self, copper):
    ANSWER: class Color(object):
    	def __init__(self, copper)


    From crown get the bat function, call it with params self, branch, bee.
    > crown.bat(branch, bee)
    ANSWER: crown.bat(branch, bee)
    ```
