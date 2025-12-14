from stats import count_words, count_characters, sort_on
import sys


def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    PATH = sys.argv[1]

    word_count = count_words(get_book_text(PATH))
    character_count = count_characters(get_book_text(PATH))
    #print(type(character_count))
    character_count.sort(reverse=True, key=sort_on)
    #print(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in character_count:
        str_to_check = item["char"]
        if str_to_check.isalpha():
            print(f"{str_to_check}: {item["num"]}")
    print("============= END ===============")
        


main()
