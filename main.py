import random


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

actual_Number = random.randint(1,100)





def easy_mode():
  i = 10 
  while(i > 0):
    print(f"You have {i} attempts remaing to guess the number")
    guess = int(input("Make a guess: "))
    if i == 1 and guess != actual_Number:
      print("You've ran out've guesses you lose.")
      break
    elif guess == actual_Number:
      print(f"You got it! The answer was {actual_Number}")
      break
    elif guess < actual_Number:
      print("Too low.\nGuess Again.")
      i = i - 1
      continue
    elif guess > actual_Number:
      print("Too High.\nGuess Again.")
      i = i - 1
      continue
    
def hard_mode():
  i = 5
  while(i > 0):
    print(f"You have {i} attempts remaing to guess the number")
    guess = int(input("Make a guess: "))
    if i == 1 and guess != actual_Number:
      print("You've ran out've guesses you lose.")
      break
    elif guess == actual_Number:
      print(f"You got it! The answer was {actual_Number}.")
      break
    elif guess < actual_Number:
      print("Too low.\nGuess Again.")
      i = i - 1
      continue
    elif guess > actual_Number:
      print("Too High.\nGuess Again.")
      i = i - 1
      continue
  

if game_difficulty == "easy":
  easy_mode()
else:
  hard_mode()


