from string import ascii_lowercase

def count_words(content):
    return len(content.split())

def count_characters(content):
    lowered_contents = content.lower()
    char_count = dict()
    for c in lowered_contents:
        if c in char_count:
            char_count[c] += 1
        elif c in ascii_lowercase:
            char_count[c] = 1
        else:
            pass
    sorted_char_count = dict(sorted(char_count.items(), key = lambda item: item[1], reverse=True))
    return sorted_char_count

def main():
    library = "books/"
    with open(library + "frankenstein.txt") as f:
        file_contents = f.read()

    print(f"--- Begin report of {library + 'frankenstein.txt'} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    count = count_characters(file_contents)
    for key in count:
        print(f"The '{key}' character was found {count[key]} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
