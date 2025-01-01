def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
result=gcd(a,b)
print(f"The gcd of {a} and {b} is {result}")