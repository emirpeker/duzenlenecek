import random
# fruits=["grape","orange","strawberry","cherry","melon","pineapple","watermelon","apple"]

# for index,item in enumerate(fruits,3):
    # print(f"{index}-{item}")

randomNumber=random.randint(1,100)
remaining_attempts=5
score=100
attempt_count=0
print("Guess a number between 1 and 100")
print(f"Your starting score:{score}")

while(remaining_attempts):
    guess=int(input("Your guess:"))
    attempt_count+=1
    if(guess<1 or guess>100):
        print("Please! Enter a number between 1 and 100")
        continue
    if(guess==randomNumber):
        print(f"Congratulations! You guessed the number correctly on your {attempt_count}.attempt")
        print(f"Your total score:{score}")
        break
    elif(guess<randomNumber):
        print("Try a larger number")
    else:
        print("Try a smaller number")
    remaining_attempts-=1
    score-=15
    if(remaining_attempts>0):
        print(f"Remaining attempts:{remaining_attempts}")
        print(f"Current score:{score}")
    else:
        print(f"Unfortunately! You ran out of attempts! The number you were trying to guess was:{randomNumber}")
        print(f"Your total score:{score}")