num=input("enter the number")
i=1
s=0
while i<len(num):
    m=num[i]
    print(i**3)
    s=s+i
    i=i+1 
print(s)



num=int(input("enter the number"))
a=((num//10)//10)//10
b=(((num)//10)//10)%10
c=(num//10)%10
d=num%10
ams=a**3+b**3+c**3+d**3
if num==ams:
    print("it is amstrong number")
else:
    print("it is not amstrong")