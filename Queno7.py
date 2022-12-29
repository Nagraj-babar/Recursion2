# Write a recursive python function to calculate sum of the digits of a given number
def f1(a):
    if a==0:
        return 0
    s=(a%10)+f1(a//10)
    return s
print(f1(22))