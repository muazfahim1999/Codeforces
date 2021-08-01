import itertools
n = input()
ser = input().split()
res= []
for x in itertools.count(start=1):
    if x == int(n)+1:
        break
    else:
        res.append((int(ser.index(str(x))))+1)
print(' '.join(map(str, res)))
