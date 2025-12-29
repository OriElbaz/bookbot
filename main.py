from stats import word_count, character_count, sorted_characters, print_text_summary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def check_inputs():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def book_path():
    return sys.argv[1]


def main():
    check_inputs()
    link = book_path()
    text = get_book_text(link)
    num_of_words = word_count(text)
    char_count = character_count(text)
    sorted_char_count = sorted_characters(char_count)

    print_text_summary(sorted_char_count, num_of_words, link)
    


if __name__ == "__main__":
    main()