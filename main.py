coins = []
t = int(input())
for i in range(t):
    n = int(input())
    summ = 0
    for j in range(1, n + 1):
        summ += 2**j
        coins.append(2 ** j)
    a = 0
    b = 0

    for k in range(n // 2 + 1):
        a += coins[k]
    a += coins[-1]
    b = summ - a
    print(abs(b - a))
    coins = []
