def rabbits_recurrence(n, k, memo):
    if memo[n] is not None:
        return memo[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = rabbits_recurrence(n-1, k, memo) + k * rabbits_recurrence(n-2, k, memo)
    memo[n] = result
    return result

def rabbit_memo(n, k):
    memo = [None] * (n + 1)
    return rabbits_recurrence(n, k, memo)


with open('rosalind_fib.txt') as f:
    data = f.read()
    n, k = data.split()
    print(rabbit_memo(int(n), int(k)))

print(rabbit_memo(6, 3))