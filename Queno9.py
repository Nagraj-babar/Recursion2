# Write a recursive python function to print octal of a given decimal number
def f1(a):
    if a>0:
        f1(a//8)
        s=print(a%8,end='')
        return s
print(f1(127))