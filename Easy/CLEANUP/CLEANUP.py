t = int(input())
while t:
    x, y = input().split()
    l = list(map(int, input().split()))
    c = []
    a = []
    for i in range(1, int(x) + 1):
        if(i in l):
            continue
        else:
            if(len(c) == 0 or len(c) == len(a)):
                c.append(i)
            elif(len(a) > len(c)):
                c.append(i)
            else:
                a.append(i)
    print(*c)
    print(*a)

    t -= 1
