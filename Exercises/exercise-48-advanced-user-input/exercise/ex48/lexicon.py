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
