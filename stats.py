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