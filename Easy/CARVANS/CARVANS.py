for k in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 1
    fast = a[0]
    for i in range(1, n):
        if fast > a[i]:
            count += 1
            fast = a[i]
    print(count)
