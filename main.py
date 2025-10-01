from stats import count_words, count_character

# Funktion liest Text aus txt. Datei
def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            file_contents = str(file_contents)
            return(file_contents)

# Ruft auslese Funktion auf   
def main(path_to_file):
    path = path_to_file
    text = get_book_text(path)
    words = count_words(text)
    characters = count_character(text)
    print(f"Found {words} total words")
    print(characters)

main("/home/jansen89/bookbot/github.com/Jansen1989/bookbot/books/frankenstein.txt")