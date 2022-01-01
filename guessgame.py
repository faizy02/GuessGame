import random 
import time

def humanGuess(x):
    random_number = random.randint(1, x)
    while 1:
        user_input = int(input("Enter your guess:"))
        if user_input > random_number:
            print("Your guess is a bit higher")
        elif user_input < random_number:
            print("Your guess is a bit lower")
        else:
            print(f"You have successfully guessed the number {user_input}")
            break

def computerGuess(y):
    print("You think of a number and now computer will try to guess it\n")
    
    low = 1
    high = int(y)
    
    while 1:
        random_number = random.randint(low, high)
        user_feedback = input(f"Is the number {random_number} Higher(H), Lower(L) or Correct(C) ?").lower()

        if user_feedback == 'h':
            high = random_number
        elif user_feedback == 'l':
            low = random_number
        elif user_feedback == 'c':
            print("Yayyy, computer has guessed the number\n")
            break

def computerVsHumanAuto(x):
    humanGuessNumber = random.randint(1, x)
    low = 1
    high = x
    turn = 0
    while 1:
        random_number = random.randint(low, high)
        print(f"\nIs the number {random_number} Higher, Lower or Correct ?")
        time.sleep(0.25)
        if random_number > humanGuessNumber:
            print(f"Its Higher")
            high = random_number
        elif random_number < humanGuessNumber:
            print(f"Its Lower")
            low = random_number
        elif random_number == humanGuessNumber:
            print(f"Yayyy, computer has guessed the number in {turn} turns\n")
            break
        turn = turn + 1


#humanGuess(1000)
#computerGuess(1000)
computerVsHumanAuto(1000)