t = int(input())

for j in range(t):
    n = int(input())
    d = []
    for i in range(n):
        d.append([int(i) for i in input().split()])
    d.sort()
    if d[0][1] % 2 == 0:
        k = d[0][0] + d[0][1] // 2 - 1
    else:
        k = d[0][0] + d[0][1] // 2
    mk = k
    for i in range(1, n):
        if d[i][1] % 2 == 0:
            k = d[i][0] + d[i][1] // 2 - 1
        else:
            k = d[i][0] + d[i][1] // 2
        if k < mk:
            mk = k

    print(mk)
