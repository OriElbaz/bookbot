from collections import defaultdict

def word_count(text: str) -> list[str]:
    return len(text.split())


def character_count(text: str) -> dict:
    characters = defaultdict(int)
    new_text = text.lower()
    
    for char in new_text:
        characters[char] += 1

    return characters
        

def sorted_characters(char_count: dict) -> list:
    d = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    key_value = d.items()
    output = []
    for each in key_value:
        if each[0].isalpha():
            d2 = {"char": each[0], "num": each[1]}
            output.append(d2)
    return output


def print_text_summary(chars: dict, word_count: int, text_link: str) -> None:
    print("========== BOOKBOT ==========")
    print(f"Analysing book found at {text_link}")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count ----------")
    for d in chars:
        print(f"{d["char"]}: {d["num"]}")



def main():
    dictionary = character_count("hello my friend")
    # print(dictionary)



if __name__ == "__main__":
    main()