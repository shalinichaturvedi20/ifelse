num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
num4=int(input("enter the number"))
if num1>num2 and num1>num3 and num1>num4:
    print("greatest number is",num1,num2,num3)
elif num2>num1 and num2>num3 and num2>num4:
    print("greatest number is",num2,num3,num4)
elif num3>num2 and num3>num1 and num3>num4:
    print("greatest number is",num3,num4,num1)
elif num4>num3 and num4>num2 and num4>num1:
    print("greatest number is",num4,num3,num2)
else:
    ("greatest number")        