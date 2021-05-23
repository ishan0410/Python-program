n=30
i=0
while (i<5):
    i=i+1
    print("Enter the number from 1 to 50: ")
    n1=int(input())
    if n1>50:
        print("You have entered more than 50")
        print ("Number of guesses left",5-i)
        continue
    if n1>n:
        print("Number is less than ",n1)
        print("Number of guesses left ",5-i)
        continue
    elif n1<n:
        print("Number is greater than ",n1)
        print("Number of guesses left ",5-i)
        continue
    else:
        print("Congratulations you have got the number!")
        print("Number of guesses you took: ",i)
        break
if i==5:
    print("You have guessed 5 times. So game over.")
    