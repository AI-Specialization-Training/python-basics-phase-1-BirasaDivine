# Write a program that:

# 1. Writes a **recursive function** `fibonacci(n)` that returns the nth fibonacci number
# 2. Writes the **same function with memoization** `fibonacci_fast(n)`
# 3. Test both with `n = 10`

memo={}
def fibonacci_fast(n):
    if n in memo:          
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_fast(n-1) + fibonacci_fast(n-2)
    return memo[n]
    