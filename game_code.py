
#                         Game - Rock,Paper,Scissors

import random
import time

options=["R","P","S"]
comp=random.choice(options)

score_user=0
score_computer=0
print("Total no. of rounds are 10")
for r in range(1,11):
    user=str(input("Enter R,P,S for Rock,Paper,Scissors respectively: \n"))
    if (user=='R' and comp=='P'):
       print("Computer won!")
       score_computer=score_computer+1
    elif (user=='R' and comp=='S'):
        print("You won!")
        score_user=score_user+1

    elif (user==comp):
         print("It's Tie!")
    elif (user=='P' and comp=='R'):
         print("You won!")
         score_user = score_user + 1
    elif (user=='P' and comp=='S'):
        print("Computer won!")
        score_computer = score_computer + 1

    elif (user=='S'and comp=='R'):
        print("Computer won!")
        score_computer = score_computer + 1
    elif (user=='S' and comp=='P'):
         print("You won!")
         score_user = score_user + 1
    print(f"{10 - r} Rounds left......")
    r=r+1

print("Calculating result...................")
time.sleep((2))

print(f"Computer's Scores are: {score_computer}, and Your scores are:{score_user}")
if score_user>score_computer:
    print("Congratulations,You won!")
else:
    print("Sorry,You lose!")

