# Write a recursive python function to print binary of a given decimal number.
def f1(a):
    if a>=1:      
        f1(a//2)
        print(a%2)

     
     
    
print(f1(11))