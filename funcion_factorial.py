def factorial(n):
    f=1
    if n!=0:
        for i in range(1,n+1):
            f=f*i
    return f