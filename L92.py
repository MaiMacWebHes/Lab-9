# L92
# Gwyneth Gangwer, Mairi Weber-Hess

def word_triangle(word):
    length = len(word)
    while length > 0:
        print(word[:length])
        length -= 1

print(word_triangle("balloons"))