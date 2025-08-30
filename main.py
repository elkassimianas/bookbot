from stats import get_num_words
from stats import get_num_character
from stats import sort_list_dict
import sys

def get_book_text(path):
    file_contents = ""

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():
    try:
        text = ""
        num_words = 0
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")

        print("----------- Word Count ----------")
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")

        print("--------- Character Count -------")
        count_characters = get_num_character(text)
#    print(count_characters)
        list_sort_characters_dicts = sort_list_dict(count_characters)
        for dict in list_sort_characters_dicts:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
    
        print("============= END ===============")
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return

main()
