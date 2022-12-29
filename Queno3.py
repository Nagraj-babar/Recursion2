# Write a recursive python function to calculate sum of first N even natural numbers
def f1(a):
    if a==2:
        return 2
    s=a+f1(a-2)
    return s
print(f1(6))