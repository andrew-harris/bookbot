def main():

    def word_counter(file_contents):
        word_list = file_contents.split()
        return len(word_list)

    def char_count(file_contents):
        characters = {}
        for char in file_contents :
            if char.isalpha() == True:
                if char.lower() not in characters:
                    characters[char.lower()] = 1
                else:
                    characters[char.lower()] += 1 
        return characters
    
    def sort_on(d):
        return d["num"]

    def dict_sort(char_dict):
        sorted_list = []
        for char in char_dict:
            sorted_list.append({"char": char, "num": char_dict[char]})
        sorted_list.sort(reverse=True, key=sort_on)
        return sorted_list
   
    word_count = 0
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    word_count = word_counter(file_contents) 
    print(word_count)
    char_dict = char_count(file_contents)
    dict_sort_chars = dict_sort(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count}  words found in the document")
    print("")
    for char in dict_sort_chars:
        print(f"The {char["char"]} character was found {char["num"]} times")

main()