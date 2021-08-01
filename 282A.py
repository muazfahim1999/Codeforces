n = int(input())
x = 0
num = [] 
for y in range(n):
    num.append(input())
for y in num:
    if y == '++X' or y == 'X++':
        x += 1
    if y == '--X' or y == 'X--':
        x -= 1
    
print(x)


