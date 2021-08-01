n , k = map(int , input().split()) 
result = 0
num = []
for n in range(1):
    num.append(input().split())
    
    
z =  num[0][k-1]
for y in num[n]:
    if int(y)!=0 and int(y) >= int(z):
        result += 1

print(result)



