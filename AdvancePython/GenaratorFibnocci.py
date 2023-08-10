"""Write a generator, that generates Fibonacci numbers. The function takes a number as argument
and generates numbers less than or equal to that number"""

a = int(input('Give amount: '))

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

b = fib()

for i in range(a):
    print (next(b))