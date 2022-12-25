def mortal_rabbits(n, m):
    alive = [1, 1]
    for i in range(2, n):
        fib = alive[i - 1] + alive[i - 2]
        if i == m:
            fib-= 1
        if i > m:
            fib-= alive[i - m - 1]
        alive.append(fib)

    return alive[-1]         

print(mortal_rabbits(88, 20))