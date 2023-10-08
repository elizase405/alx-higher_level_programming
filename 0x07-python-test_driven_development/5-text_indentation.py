#!/usr/bin/python3
"""
The text_indentation module contains 1 function: text_indentation(text)
"""


def text_indentation(text):
    """
    prints text and adds 2 newline
    anywhere a '.', '?', or ':' is encountered.

    Args:
        text (str) string to be printed

    Raises:
        TypeError: raised if text inputted is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
