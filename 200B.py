n = int(input())
a = input().split()
res = 0
for i in range(n):
    res += int(a[i])
print(res/n)
