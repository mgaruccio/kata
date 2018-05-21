import string


def is_pangram(sentence):
    # Convert all letters in the string to lowercase
    lowerCaseSentence = sentence.lower()
    # Use the all-lowercase string as the input for creating a new set of unique characters
    uniqueLetters = set(lowerCaseSentence)
    # Filter the set to include only letters, removing all numbers and symbols
    alphaOnly = [x for x in uniqueLetters if x.isalpha()]
    # determine the length of the resulting set
    arrayLength = len(alphaOnly)
    # return the result of a comparison between the length of the array and number of letters in the alphabet
    return arrayLength == len(string.ascii_lowercase)
