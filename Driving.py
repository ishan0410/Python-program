print("Enter your age")
age = int(input())
if 18<age<=100:
    print("You are eligible for driving")
elif age==18:
    print("You have to physically come to drive and test yourself")
elif age<18: 
    print("You are not eligible for driving")
else:
    print("Enter a valid age")
   