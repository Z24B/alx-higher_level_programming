#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if not size:
        return (size, None)
    else:
        return (size, sentence[0])
