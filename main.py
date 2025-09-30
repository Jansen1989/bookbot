# Funktion liest Text aus txt. Datei
def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()
            return(file_contents)

# Ruft auslese Funktion auf   
def main(path_to_file):
    path = path_to_file
    text = get_book_text(path)
    print(text)

main("/home/jansen89/bookbot/github.com/Jansen1989/bookbot/books/frankenstein.txt")