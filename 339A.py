a = input()
num = ''
for x in a:
    if x.isdigit():
        num += x
z = sorted(num)
listToStr = '+'.join(map(map, z))
print(listToStr)

