

def search_letter(example_string):
    separated_string = example_string.split()
    result_string = ''
    for word in separated_string:
        if word.istitle():
            result_string += word[0]
    return print(result_string)


example_string = "How are you? Eh, ok. Low or Lower? Ohhh."
search_letter(example_string)
