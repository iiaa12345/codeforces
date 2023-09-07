t = int(input())

for i in range(t):
    a, b, c = [float(i) for i in input().split()]
    cnt = 0
    if a < b:
        while a < b:
            a += c
            b -= c
            cnt += 1
    elif a > b:
        while a > b:
            a -= c
            b += c
            cnt += 1
    
    print(cnt)
