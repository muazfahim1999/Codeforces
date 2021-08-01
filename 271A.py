import itertools
n = int(input())
m = n+1
s = list(str(m))
for x in itertools.count(start=0):
    if s.count(s[0]) > 1 or s.count(s[1]) > 1 or s.count(s[2]) > 1 or s.count(s[3]) > 1:
        m = m + 1
        s = list(str(m))
    else:
        print(m)
        break

    
