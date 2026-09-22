import random
game_number = random.randint(1,10)
guess_count = 0
#print(game_number)
while(1):
    guess = int(input("Enter a number between 1 and 10: "))
    guess_count += 1
    if guess > game_number: 
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else:
        print("You Win")
        print(f"It took you {guess_count} guesses.")
    if guess_count >= 5:
        print("Wow you are really bad at this game!")
        break