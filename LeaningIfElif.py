print("Enter the first no")
var1=int(input())
print("Enter the second no")
var2=int(input())
if var1>=var2:
    print(var1," is greater than ",var2)
elif var1==var2:
    print(var1," is equal to ",var2)
else:
    print(var1," is lesser than ",var2)

l1=[2,3,4,5]
print("Enter a no")
var3=int(input())
if var3 in l1:
    print(var3," is in the list")
else:
    print(var3," is not in the list")

print("Enter your age")
age=int(input())
if age>18 and age<100:
    print("Your age is valid for driving")
elif age>7 and age<18:
    print("Your age is not valid for the driving")
elif age==18:
    print("We cannot decide.You have to come for the physical test")
else:
    print("Invalid age entered")
