print("Enter the numbers: ")
a=int(input())
b=int(input())
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
opr = int(input("Enter the operator number: "))
if a==45 and b==3 and opr==3:
    print(555)
elif a==56 and b==9 and opr==1:
    print(77)
elif a==56 and b==6 and opr==4:
    print(4)
elif opr==1:
    print(a+b)
elif opr==2:
    print(a-b)
elif opr==3:
    print(a*b)
elif opr==4:
    print(a/b)
else:
    print("Enter valid inputs.")

