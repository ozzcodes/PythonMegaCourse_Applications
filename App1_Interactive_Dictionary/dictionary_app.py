import json
from difflib import get_close_matches

dictionary_data = json.load(open('resources/dictionary.json'))
choose_yes = ['yes', 'y']
choose_no = ['no', 'n']


def dictionary_app(get_word: str):
    """
    Args:
        get_word (str):
    """
    if get_word in dictionary_data:
        return dictionary_data[get_word]
    elif get_word not in dictionary_data:
        if get_word.upper() in dictionary_data:
            return dictionary_data[get_word.upper().strip()]
        elif get_word.lower() in dictionary_data:
            return dictionary_data[get_word.lower().strip()]
        resp = "The word you entered doesn't exist! Would you like to enter another word? (y/n)".lower().strip()
        get_resp = input(resp)
        if get_resp in choose_yes:
            input('Please enter a word: (Check for proper spelling!) ')
            new_word = get_close_matches(user_input, dictionary_data.keys())[0]
            print(new_word)
            return dictionary_data[new_word]
        elif get_resp in choose_no:
            # exit loop
            print('Thank you for using the Python Dictionary Program!')
            exit(0)
        else:
            pass

    else:
        "Thank you for using the Dictionary Program!"


get_input = input('Please Enter a word: ')
user_input = get_input.lower().strip()

output = dictionary_app(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
