import itertools
n = input()
b = list(n)
a=[]
c = n.count("4")
d = n.count("7")
if int(c+d) == 4 or  int(c+d) == 7:
    res = 'YES'
else:
    res = 'NO'
print(res)
