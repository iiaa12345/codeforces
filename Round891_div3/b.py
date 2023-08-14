t = int(input())

for ti in range(t):
    x = list(map(int, list(input())))
    while True:
        fl = True
        for i in range(len(x)):
            if x[i] >= 5:
                fl = False
                if i == 0:
                    x = [1] + [0] * len(x)
                else:
                    x[i - 1] += 1
                    for j in range(i, len(x)):
                        x[j] = 0
        if fl:
            break
                
    print(int("".join(map(str, x))))
