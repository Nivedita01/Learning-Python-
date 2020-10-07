def fib(n):
    if(n <= 1):
        return n
    return fib(n - 1) + fib(n - 2)
    
x = int(raw_input ("Enter an integer: "))
print fib(x)