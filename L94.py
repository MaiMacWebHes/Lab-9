# L94
# Gwyneth Gangwer, Mairi Weber-Hess

index = 0        # sets the index at 0
s = "Mind the gap!"     # assigns "Mind the gap!" variable "s"
while index < len(s) and s[index] != "":       # while the index is less than the length of s and s of index is not equal 0.
    index += 1      # reassigns index to one higher than it was
print(s[:index])    # prints s starting at first character and going to the character indicated by the index

# D: untiL_dot (using while)

def until_dot(x):
    def find_period(y):
        index = 0
        while index < len(y):
            for ch in y:
                if ch == ".":
                    return index
                else:
                    index += 1

    location = find_period(x)

    return x[:location]

print(until_dot("This. That."))
print(until_dot("192.168.200.2"))
print(until_dot("No dots here"))

# Break on through

def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("YOu told me that word already!")
            break
        words.append(word)
    return words

# Which of these approaches do you think would work to fix the bug? (only one of them is correct.)
# - Don't use break at all here. Just move the return statement to where the break is now.