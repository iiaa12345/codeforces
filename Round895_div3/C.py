t = int(input())

for i in range(t):
    l, r = [int(i) for i in input().split()]
    fl = False
    for i in range(2, r - 1):
        a = l - i
        b = i
        if a > 0 and b > 0:
            if a > b:
                if a // b * b + a % b > 1 and b // (a % b) * (a % b) + b % (a % b) > 1:
                    fl = True
                    break
            if b > a:
                if b // a * a + b % a > 1 and  b // (b % a) * (b % a) + a % (b % a) > 1:
                    fl = True
                    break
    if fl:
        print(a, b)
    else:
        print(-1)
