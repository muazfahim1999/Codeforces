n = int(input())
a = input()
b = list(a)
d = b[1:]
c = 0
for x in range(n-1):
    if b[x] == d[x]:
        c += 1
print(c)


