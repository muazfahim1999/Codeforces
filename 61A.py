a = list(input())
b = list(input())
c = []
for x in range (len(a)):
    if a[x] == b[x]:
        c.insert(x,"0")
    else:
        c.insert(x,"1")
        
print("".join(c))
