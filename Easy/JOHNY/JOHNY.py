t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    element = a[k - 1]
    print(sorted(a).index(element) + 1)
    t -= 1
