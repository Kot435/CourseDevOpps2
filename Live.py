# from MainGame import a
# from MemoryGame import play
import random
val = 0
val_difficulty = 0

name = input("Enter Name...")

def welcome(name):
    print("Hello", name, "and welcome to the World of Games (WoG)./n Here you can find many cool games to play.")

def load_game():
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer")

    user_number = input("Please choose a game to play...:")
    try:
        val = int(user_number)
        if (val > 0 and val <= 2):
            game_difficulty(val)
        else:
            print("You must enter a number 1 OR 2")
            load_game()
    except ValueError:
        print("No.. input number")


def game_difficulty(val):
    game_difficulty = input("Please choose game difficulty from 1 to 5:")
    try:
        val_difficulty = int(game_difficulty)
        if (val_difficulty > 0 and val_difficulty <= 5):
            if(val == 1):
                play(val,val_difficulty)
                add_score(val_difficulty)
        else:
            print("You must enter a between 1 to 5")
            game_difficulty()
    except ValueError:
        print("No.. input number")

def play(val,val_difficulty):
    print(val,val_difficulty)
    print(random.sample(range(1, 100), 3))
    for x in range(val_difficulty):
        print("random", random.randint(1, 101))

# def get_list_from_user(val_difficulty):


# def is_list_equal(list_a, list_b):


def add_score(val_difficulty):
# Create a text file named “words.txt”
    file = open("F:\\DevOpps\\score.txt",'w')
    file.close()

    file = open("F:\\DevOpps\\score.txt",'w')
    file.write(str(val_difficulty))
    file.close()


if __name__ == '__main__':
    welcome(name)
    load_game()
