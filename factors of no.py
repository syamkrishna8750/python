n=int(input("Enter a number:"))
print("The factors of",n)
for x in range(1,n+1):
    if n%x==0:
        print(x)