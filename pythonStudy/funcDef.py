
#function definition example
#following example is a
def fib(n) :
    """print fibonacci sequence where all the numbers are all under n"""
    a,b = 1,1
    while a<n :
        print(a, end=" ")
        a, b = b, a+b

fib(10)
