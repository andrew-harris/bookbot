def get_num_words(file_contents):
    counter = 0
    text = file_contents.split()
    for word in text:
        counter +=1
    return counter

def get_character_count(book):
    output = {}

    for char in book: 
        lchar = char.lower()
        if lchar in output:
            output[lchar] += 1
        else:
            output[lchar] = 1
    return output

def get_sorted_count(unsorted_dict):
    new_list = []
    for char, count in unsorted_dict.items():
        char_dict = {"char": char, "count": count}
        new_list.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]

    new_list.sort(reverse=True, key=sort_on)
    return new_list
