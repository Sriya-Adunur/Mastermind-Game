# Defines functions for input and output.
# CSC 101, Project 3
# Given code, Summer '22

def parse_integer(string, default):
    """
    Extract an integer from a string.
    TODO: Debug this function.

    :param string: An arbitrary string
    :param default: A default value
    :return: The result of converting the string to an integer, or the default
             value if the string does not consist only of decimal digits
    
    if not string.isalpha():
        return int(string)
    else:
        return default
    """

    if not string.isnumeric():
        return default
    else:
        if int(string) < 0:
            return default
        else:
            return int(string) 

def parse_character(string, default):
    """
    Extract an uppercase alphabetical character from a string.
    TODO: Debug this function.

    :param string: An arbitrary string
    :param default: A default value
    :return: The first alphabetical character in the string, uppercased, or the
             default value if there are no alphabetical characters
    
    for character in string:
        if character.isalpha():
            return character.upper()
        else:
            return default
    """

    for character in string:
        if character.isalpha():
            return character.upper()
    return default


def parse_string(string, length):
    """
    Extract an uppercase alphabetical string from a string.
    TODO: Debug this function.

    :param string: An arbitrary string
    :param length: A desired number of characters
    :return: The alphabetical characters in the string, uppercased and in the
             order they appeared, not exceeding the desired length
  
    guess = ""

    for i in range(length):
        if string[i].isalpha():
            guess = guess + string[i].upper()

    return guess
    """
    
    lst = []
    for char in string:
        if char.isalpha():
            lst.append(char)

    g = ""
    for x in lst:
        g += x

    g1 = ""    

    for i in range(min(len(g), length)):
        if g[i].isalpha():
            g1 = g1 + g[i].upper()
    return g1
 
