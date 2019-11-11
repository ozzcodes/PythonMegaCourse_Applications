# Building a Maker-Function
def sentence_maker(phrase):
    """
    Args:
        phrase:
    """
    capitalized = phrase.capitalize()
    interrogatives = ('how', 'what', 'why', 'where', 'when')
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


# Test the function
# print(sentence_maker("how are you"))

# Constructing the Loop
results = []
while True:
    user_input = input('Say something: ')
    if user_input == "q":
        break
    else:
        results.append(sentence_maker(user_input))

print(' '.join(results))
