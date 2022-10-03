s = input()
str_new = ''
for i in s:
    if str_new.find(s[i]) == -1 and s[i] != ' ':
        str_new = s[i] + str_new
print(str_new)