k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
res = 0
for x in range(1,d+1):
    if x%k==0 or x%l==0 or x%m==0 or x%n==0:
        res+=1
print(res)
