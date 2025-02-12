"""
Invertir palabras de una cadena dada.
"""


def flip_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


sentence = input("If you give me a sentence, I will reverse the order of its words: ")

print("Here you go:", flip_words(sentence))
