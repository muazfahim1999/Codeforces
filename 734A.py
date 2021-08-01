n = int(input())
serial = input()
a = serial.count("A")
d = serial.count("D")
if a > d :
    print("Anton")
elif a == d:
    print("Friendship")
else:
    print("Danik")
