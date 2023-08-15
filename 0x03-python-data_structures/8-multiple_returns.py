#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if len <= 0:
        return 'None'
    return len(sentence), sentence[0]
