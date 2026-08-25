# Fibonacci using memoization

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    # Base cases 
    if n <= 1:
        return n

    #Return already calculated Value
    if n in memo:
        return memo[n]

    #Calculate and store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]



# Input
n = int(input("Enter n: "))

print("Fibonacci number using Memoization:",fibonacci_memo(n))