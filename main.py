from stats import get_num_words
from stats import get_num_character
from stats import sort_list_dict

def get_book_text(path):
    file_contents = ""

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():
    text = ""
    num_words = 0
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    text = get_book_text("books/frankenstein.txt")
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

    return

main()
