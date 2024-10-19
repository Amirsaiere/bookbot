def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_dict = get_char_count(book_text)
    print_report(word_count,char_dict,book_path)


def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()

def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def get_char_count(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for char in book_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def print_report(word_count,char_dict,book_path):
    print(f"--- Begin report of {book_path} ---", end ="\n\n")
    print(f"{word_count} words found in the document")
    print()
    for char,count in char_dict.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")
    
main()
