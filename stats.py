# Funktion zum Wörter zählen
def count_words(text):
    words = len(text.split())
    return words

def count_character(text):
    text_lower = text.lower()
    characters = {}
    for c in text_lower:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_on(characters):
    result = []
    for c in characters:
        count = characters[c]
        result.append({"char": c, "num": count})
    return result

def sort_helper(item):
    return item["num"]