# Write a recursive python function to find the Nth term of the Fibonacci series.
def f1(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        x= f1(a-1)+f1(a-2)
        return x
n=int(input('Enter a number: '))
print(f1(n))