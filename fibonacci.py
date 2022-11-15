fin = int(input('\nCuántos números de la sucesion de Fibonacci quiere que muestre?: '))
fib1 = 0
fib2 = 1
for i in range(fin):
    fib3 = fib1 + fib2
    print(fib3, end =',')
    fib1 = fib2
    fib2 = fib3