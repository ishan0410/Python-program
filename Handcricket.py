print("   ***Hand Cricket***   ")
sum=0
import random
wicket=0
compruns=0
print(" 1st innings: (Batting) ")
while wicket<2:
    print("My choice: ",end="")
    mychoice=int(input())
    lst=[1,2,3,4,5,6]
    compchoice=random.choice(lst)
    if mychoice in lst:
        print("Computer's choice: ",compchoice)
        if mychoice==compchoice:
            print("Wicket!")
            wicket+=1
            print("Target :",sum+1)
            break
        sum+=mychoice
        print("Runs: ",sum)
    else :
        print("Enter a valid number!")
        continue
target=sum-compchoice+1
print(" 2nd innings: (Bowling) ")
wicket=0
while wicket<2:
    print("My choice: ",end="")
    mychoice=int(input())
    lst=[1,2,3,4,5,6]
    compchoice=random.choice(lst)
    if mychoice in lst:
        print("Computer's choice: ",compchoice)
        if mychoice==compchoice:
            print("Wicket!")
            print("You Win!")
            wicket+=1
            break
        compruns+=compchoice
        print("Runs: ",compruns)
        if compruns>target:
            print("Computer Wins!")
            break    
    else :
       print("Enter a valid number!")
       continue
