def count_each_character(input_string): # returns a dictionary
    char_dict = {}
    for character in input_string:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict


def anagramStrings(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    return count_each_character(first_string) == count_each_character(second_string)

if __name__ == '__main__':
    print(anagramStrings('zahash', 'hazash'))
    print(anagramStrings('zahash', 'hazas'))

