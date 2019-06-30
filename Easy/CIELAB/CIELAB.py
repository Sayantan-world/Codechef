x, y = input().split()
s = int(x) - int(y)

if(s > 0):
    s += 1
    if(s % 10 == 0):
        s -= 2
    print(s)
else:
    s -= 1
    if(s % 10 == 0):
        s += 2
    print(s)
