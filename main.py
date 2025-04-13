

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    import sys
    from stats import get_num_words, get_character_count
    from stats import get_sorted_count
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    filepath = sys.argv[1]

    file_contents = get_book_text(filepath)
    character_count = get_character_count(file_contents)

    word_count = get_num_words(file_contents)

    sorted = get_sorted_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")

main()
