def fib_recursively(n: int) -> int:
    # sourcery skip: assign-if-exp, reintroduce-else
    if n <= 1:
        return n
    
    return fib_recursively(n - 1) + fib_recursively(n - 2)


fib_cache = {
    0: 0,
    1: 1,
}
def fib_cache(n: int) -> int:
    if n in fib_cache:
        return fib_cache[n]
    
    fib_cache[n] = fib_cache(n - 1) + fib_cache(n - 2)
    return fib_cache[n]


def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, (a + b)
    
    return b