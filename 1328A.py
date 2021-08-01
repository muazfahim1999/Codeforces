n = int(input())
a = []
b = []
for x in range(n):
    a.append(input().split())

for x in range(n):
        i = (int(a[x][0]))%(int(a[x][1]))
        if i==0 :
            b.append(i)
        else:
            b.append(((int(a[x][1]))-i))
for x in range(n):
    print(b[x])

