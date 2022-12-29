# Write a recursive python function to calculate the factorial of a number.
def f1(a):
    if a==1:
        return 1
    s=a*f1(a-1)
    return s
b=int(input('Entre a number: '))
print(f1(b))