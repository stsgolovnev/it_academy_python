s = input()
low_word = 0
up_word = 0
for i in s:
    if 'a' <= i <= 'z':
        low_word = low_word + 1
    elif 'A' <= i <= 'Z':
            up_word = up_word + 1
print(low_word)
print(up_word)