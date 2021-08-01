k,n,w = map(int,input().split())
total_cost =  (w*(w+1)/2*k)
borrow = total_cost - n
if borrow > 0:
    print(int(borrow))
else:
    print("0")

