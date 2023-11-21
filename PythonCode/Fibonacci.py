def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


num_terms = int(input("Enter the number of terms in the Fibonacci series: "))


print("Fibonacci Series:")
print(fibonacci(num_terms))
