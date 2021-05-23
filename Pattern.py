# print("How Many Rows You Want To Print: ")
# one= int(input())
# print("Type 1 Or 0: ")
# two = int(input())
# new =bool(two)
# if new == 1:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new == 0:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*", end=" ")
print("Enter number of rows: ")
n=int(input())
i=0
a=int(input("Enter number 1 or 0: "))
if a==1:
    while i<=n:
        print("* "*i,end=" ")
        print("\n",end="")
        i=i+1
elif a==0:
    i=n
    while i!=0:
        print("* "*i,end=" ")
        print("\n",end="")
        i=i-1