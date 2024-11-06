# L91
# Gwyneth Gangwer, Mairi Weber-Hess

# A: Total Length
def total_length(x):
    total = 0
    for ch in x:
        total += len(ch)
    return total

a = total_length(['Queen', 'rules'])
b = total_length([])
c = total_length(['balloons'])
d = total_length(["",'',"",''])

print(a,b,c,d)

s = "Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])