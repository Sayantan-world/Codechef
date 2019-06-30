def z(n):
    zeros = 0
    i = 1
    while n // 5**i > 0:
        zeros += n // 5**i
        i += 1
    return zeros


t = int(input())
while t:
    n = int(input())
    print(z(n))
    t = t - 1
