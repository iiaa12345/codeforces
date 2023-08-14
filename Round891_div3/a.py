t = int(input())

for ti in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[1] % 2 == (sum(a) - a[1]) % 2:
        print("YES")
    else:
        print("no")
