# Write a recursive python function to calculate sum of first N natural numbers
def f1(n):
    if n==1:
        return n
    return n+f1(n-1)
a=int(input('Enter a number: '))
print(f1(a))
