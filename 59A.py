a = input()
b = list(a)
c = []
d = []
for i in range(len(b)):
    if b[i].isupper():
        c.append(b[i])
    else:
        d.append(b[i])
if len(c) > len (d):
    res = a.upper()
else:
    res = a.lower()
print(res)
