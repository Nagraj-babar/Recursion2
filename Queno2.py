# Write a recursive python function to calculate sum of first N odd natural numbers
def f1(a):
    if a==1:
        return 1
    s=a+f1(a-2)
    return s
b=int(input("Enter a odd number: "))
print(f1(b))
    
    




    
