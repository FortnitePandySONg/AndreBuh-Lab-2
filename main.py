import random
game_number = random.randint(1,100)
#print(game_number)
while(1):
    guess = int(input("Enter a number between 1 and 100: "))
    if guess > game_number: 
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else:
        print("You Win")
        break