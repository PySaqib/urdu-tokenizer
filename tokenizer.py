#!/bin/python3

# Urdu Tokenizer.
# I am still trying to figure out a way to eradicate the seperation of text in output.

data = "کیا حال ہے آپ کا؟"  # Add any Urdu text here.

def tokenize(data):
    token = []

    word = ''

    for c in data:
        if (c != ' '):
            word += c
        else:
            token.append(word[::-1]) # "word[::-1]" makes sure that characters are appended in the the correct order.
            word = ''

    return(token)

print(tokenize(data))