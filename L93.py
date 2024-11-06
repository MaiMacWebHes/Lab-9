# L93
# Gwyneth Gangwer, Mairi Weber-Hess

def count_character(word, char):
    count = 0
    index = 0
    while index < len(word):
        if word [index] == char:
            count += 1
        index += 1
    return count

print(count_character("bonobos", "o"))