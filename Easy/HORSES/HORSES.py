t = int(input())
while t:
    diff = 10**20
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    for i in range(n - 1):
        if arr[i + 1] - arr[i] < diff:
            diff = arr[i + 1] - arr[i]
    t -= 1
    print(diff)
