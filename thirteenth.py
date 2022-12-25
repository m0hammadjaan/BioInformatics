def fib(n):
    memo = [None] * (n + 1)
    if memo[n] is not None:
        return memo[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result
with open('rosalind_fibo.txt') as f:
    print(fib(int(f.read())))