# Funktion liest Text aus txt. Datei
def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            file_contents = str(file_contents)
            return(file_contents)


# Funktion zum Wörter zählen
def count_words(text):
    words = len(text.split())
    return words




# Ruft auslese Funktion auf   
def main(path_to_file):
    path = path_to_file
    text = get_book_text(path)
    
    
    print(count_words(text))

main("/home/jansen89/bookbot/github.com/Jansen1989/bookbot/books/frankenstein.txt")