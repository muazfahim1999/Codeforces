n = int (input())
words = []
for x in range(n):
    words.append(str(input()))
for x in range(n):
    if len(words[x]) > 10:
        words[x] = words[x][:1] + str(len((words[x]))-2) + words[x][-1]
    else:
        words[x] = words [x]
for x in range(n):
    print(words[x])


