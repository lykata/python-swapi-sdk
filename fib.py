def fib(x) -> int:
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)