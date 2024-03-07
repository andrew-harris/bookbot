def main():

    word_list = []
    breakdown = {}


    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    word_list = file_contents.split()

    for word in word_list:
        character = []
        for char in word:
            if char.isalpha() == True:
                breakdown[char] = 1
    print(breakdown)

main()