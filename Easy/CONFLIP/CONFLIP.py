t = int(input())
while t:
    games = int(input())
    while games:
        x, y, z = map(int, input().split())
        if(x == z):
            print(y // 2)
        else:
            print(y - y // 2)
        games -= 1
    t -= 1
