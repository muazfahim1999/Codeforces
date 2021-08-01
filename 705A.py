import itertools
n = int(input())
sen = ['I' , 'hate' , 'it']
for x in itertools.count(start=2):
    if x > n :
        break
    else:
        if x % 2 == 0:
            sen.insert(-1,"that I love")
        else:
            sen.insert(-1,"that I hate")
print(" ".join(sen))
