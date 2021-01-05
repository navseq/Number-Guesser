from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print("You guessed the correct number.")

def set_difficulty():
  level = input("Choose a difficuty level. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 to 100")

  answer = randint(1, 100)
  print(f"The guessed number is {answer}")

  turns = set_difficulty()  

  guess = 0
  while answer != guess:
    print(f"You have {turns} attempts remaining.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses")
      return
      
game()
