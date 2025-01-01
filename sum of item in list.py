l=[]
n=int(input("Enter a limit:"))
for i in range (n):
    v=int(input("Enter values"))
    l.append(v)
print(l)
sum=0
for x in l:
    sum=sum+x
print("sum of all items=",sum)