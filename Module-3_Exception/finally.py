try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    print(e)
finally:
    print("This is Finally Block!")
    x=int(input("Enter X:"))
    y=int(input("Enter Y:"))
    print("Mul:",x*y)
