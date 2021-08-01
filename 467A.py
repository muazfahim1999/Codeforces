n = int(input())
s = []
res = 0
for x in range(n):
    s.append(input().split())
for x in range(n):
    if int(s[x][1]) - int(s[x][0]) > 1:
        res += 1
print(res)
