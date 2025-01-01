l=[]
n=int(input("Enter the limit:"))
for i in range(n):
    v=int(input("Enter values:"))
    l.append(v)
print(l)
c=[x for x in l if x%2!=0]
print("list of non even numbers:",c)