def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_character(text):
    lower_text = text.lower()
    character_dict = {}
    list_character_count = []

    for c in lower_text:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1

    for ch in character_dict:
        list_character_count.append({"char": ch, "num": character_dict[ch]})


    return list_character_count

def sort_on(characters):
    return characters["num"]

def sort_list_dict(count_characters):
    count_characters.sort(reverse=True, key=sort_on)
    return count_characters
