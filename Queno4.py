# Write a recursive python function to calculate sum of squares of first N natural numbers
def f1(a):
    if a==1:
        return 1
    s=a*a+f1(a-1)
    return s
print(f1(2))