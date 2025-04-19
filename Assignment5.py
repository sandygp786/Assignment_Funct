def factorial(n):
    if (n<2):
        return 1
    elif (n==2):
        return 2
    elif (n>2):
        return n * factorial(n-1)
    else:
        print("Invalid Number",n)

x=int(input("Enter a number "))
result=factorial(x)
print("Factorial of",x,"is:",result)