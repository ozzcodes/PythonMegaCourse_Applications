import json
import re

dictionary_data = json.load(open('resources/dictionary.json'))


def dictionary_app(get_word):
    if get_word in dictionary_data:
        return dictionary_data[get_word]
    else:
        if get_word not in dictionary_data:
            try_again = input("The word you entered doesn't exist! Would you like to enter another word? (y/n)")
            print(try_again)
            if try_again == 'y' or 'Y':
                new_input = input('Please Enter a word: (Check your spelling)')
                if new_input == get_word in dictionary_data:
                    return dictionary_data[new_input]
            else:
                "Thank you for using the Dictionary Program!"
        else:
            return "Thank you for using the Dictionary Program"


get_input = input('Please Enter a word: ')
user_input = get_input.lower().strip()

print(dictionary_app(user_input))
