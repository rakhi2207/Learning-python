opr=input("Enter the operation it can be +,-,*,/,%")
var1=int(input("Enter the first no"))
var2=int(input("Enter the second no"))
if opr=="*" and var1==45 and var2==3:
    result=555
elif opr=="+" and var1==56 and var2==9:
    result=77
elif opr=="/" and var1==56 and var2==6:
    result=4
elif opr=="+":
    result=var1+var2
elif opr=="-":
    result=var1-var2
elif opr=="*":
    result=var1*var2
elif opr=="/":
    result=var1/var2
elif opr=="%":
    result=var1%var2
else:
    print("Invalid operation")

print("Answer is ",result)