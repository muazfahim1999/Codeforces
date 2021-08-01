n = int(input())
result = 0
num = {}
for x in range(n):
    a,b,c = input().split()
    num[x] = a+b+c
    
for x in range(n):
    y = num[x].count("1")
    if y > 1:
        result += 1
    
print(result)



