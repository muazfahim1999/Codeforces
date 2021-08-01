n , h = input().split()
i = input().split()
res = 0
for x in range(len(i)):
    if int(i[x]) > int(h):
        res += 2
    else:
        res += 1
print(res)
