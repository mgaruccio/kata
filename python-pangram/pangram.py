# So this version is more of a joke than anything, wanted to see if I could do it in one line
# It works all right but honestly it's probably not the easiest thing to explain compared with using an array


def is_pangram(sentence):
    return len([x for x in set(sentence.lower()) if x.isalpha()]) == 26
