import random

TARGET = 12
DICE_MIN = 1
DICE_MAX = 6

def print_welcome():
    print("Welcome to Dice Game 12!")
    print("Your goal is to roll three dice and reach a total of 12.")
    print("You will roll one die at a time and can quit anytime by entering 'q'.")

def read_choice(rolled1, rolled2, rolled3):
    while True:
        choice = input("Enter 1, 2, 3, or q to quit: ")
        if choice == "q":
            return "q"
        if not choice.isdigit():
            print("Invalid input")
            continue
        choice = int(choice)
        if choice < 1 or choice > 3:
            print("Invalid input")
            continue
        elif choice == 1 and rolled1:
            print("Sorry, you already rolled that dice. Try again.")
            continue
        elif choice == 2 and rolled2:
            print("Sorry, you already rolled that dice. Try again.")
            continue
        elif choice == 3 and rolled3:
            print("Sorry, you already rolled that dice. Try again.")
            continue
        return choice


def roll_die():
    num = random.randint(DICE_MIN, DICE_MAX)
    return num

def show_state(d1, d2, d3, wins, losses):
    total = d1 + d2 + d3
    print(f"{d1} {d2} {d3} sum: {total} #win: {wins} #loss: {losses}")

def play_round(wins, losses):
    d1 = d2 = d3 = 0
    rolled1 = rolled2 = rolled3 = False
    rolls_done = 0

    while rolls_done < 3:
        choice = read_choice(rolled1, rolled2, rolled3)
        if choice == "q":
            return "quit"
        num = roll_die()
        if choice == 1:
            d1 = num
            rolled1 = True
        elif choice == 2:
            d2 = num
            rolled2 = True
        elif choice == 3:
            d3 = num
            rolled3 = True
        rolls_done += 1
        print(show_state(d1, d2, d3, wins, losses))
    total = d1 + d2 + d3
    if total == TARGET:
        print("You won!")
        return "win"
    elif total > TARGET:
        print("You lost!")
        return "loss"
    else:
        print("You neither won nor lost the game.")
        return "none"
                   
            
def main():
    print_welcome()

    wins = 0
    losses = 0

    while True:
        result = play_round(wins, losses)
        if result == "quit":
            break
        elif result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        print(f"#win: {wins} #loss: {losses}")
        print("Next round!")
    print("Game Over!")



    
if __name__ == "__main__":
    main()

