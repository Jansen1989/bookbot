from stats import count_words, count_character, sort_on, sort_helper

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
    characters = sort_on(characters)
    characters.sort(key=sort_helper, reverse = True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in characters:
         ch = item["char"]
         if ch.isalpha():
              print(f"{ch}: {item["num"]}")
    print("============= END ===============")

main("/home/jansen89/bookbot/github.com/Jansen1989/bookbot/books/frankenstein.txt")