import json
import difflib
from difflib import SequenceMatcher

dictionary_data = json.load(open('resources/dictionary.json'))
choose_yes = ['yes', 'y']
choose_no = ['no', 'n']


def dictionary_app(get_word):
    if get_word in dictionary_data:
        return dictionary_data[get_word]
    elif get_word not in dictionary_data:
        resp = input("The word you entered doesn't exist! Would you like to enter another word? (y/n)").lower().strip()
        for new_word in resp:
            if new_word == dictionary_data[new_word]:
                return dictionary_data[revised_input]

            if resp in choose_yes:
                input('Please Enter a word: (Check your spelling)')
                return dictionary_data[revised_input]
            elif resp in choose_no:
                # exit loop
                print('Thank you for using the Python Dictionary Program!')
                exit(0)
            else:
                pass
    else:
        "Thank you for using the Dictionary Program!"


get_input = input('Please Enter a word: ')
user_input = get_input.lower().strip()
revised_input = input('Please Enter a word: (Check your spelling)')
new_input = revised_input.lower().strip()


if user_input in dictionary_app(get_word=True):
    print(dictionary_app(user_input))
else:
    print(dictionary_app(revised_input))
