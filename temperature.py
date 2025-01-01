def fahrenheit_to_celcius(temp):
    return(temp-32)*5/9

def celsius_to_fahrenheit(temp):
    return(temp*9/5)+32

print("1:fahrenheit to celsius")
print("2:celsius to fahrenheit")

choice=int(input("enter your choice(1 or 2):"))

if choice==1:
    temp=float(input("enter the temperature in fahrenheit:"))

    celsius=fahrenheit_to_celcius(temp)
    print(f"the temperature in celsius is :{celsius:.2f}")
elif choice==2:
    temp=float(input("enter the temperature in celsius:"))

    fahrenheit=celsius_to_fahrenheit(temp)
    print(f"the temperature in fahrenheit is: {fahrenheit:.2f}")
else:
    print("invalid choice. please enter 1 or 2.")