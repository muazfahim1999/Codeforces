n = int(input())
s = [int(x) for x in input().split()]
maxi = max(s)
mini = min(s)
a = s.index(max(s))
b = s.index(min(s))
s.pop(a)
s.insert(0,maxi)
s.reverse()
b = s.index(mini)
res = a+b

print(res)

