import json
from difflib import get_close_matches

dictionary_data = json.load(open('resources/dictionary.json'))
choose_yes = ['yes', 'y']
choose_no = ['no', 'n']


def dictionary_app(get_word):
    """
    Args:
        get_word:
    """
    if get_word in dictionary_data:
        # Use the difflib's get_close_match function
        return dictionary_data[get_word]
    elif len(get_close_matches(get_word, dictionary_data.keys())) > 0:
        resp = 'Did you mean %s instead? (y/n)' % get_close_matches(get_word, dictionary_data.keys())[0]
        get_resp = input(resp)
        if get_resp in choose_yes:
            new_word = get_close_matches(get_input, dictionary_data.keys())[0]
            return dictionary_data[new_word]
        elif get_resp in choose_no:
            # exit loop
            print('Thank you for using the Python Dictionary Program!')
            exit(0)
        else:
            pass
    else:
        return 'Sorry that word does not exist! (Please check your spelling)'


get_input = input('Please Enter a word: ')
user_input = get_input.lower().strip()

print(dictionary_app(user_input))
