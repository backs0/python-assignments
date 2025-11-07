import random

def print_welcome():
    print("Welcome to Dice Game 12!")
    print("Your goal is to roll three dice and reach a total of 12.")
    print("You will roll one die at a time and can quit anytime by entering 'q'.")

def read_choice(rolled1, rolled2, rolled3):
    while True:
        choice = input("Enter 1, 2, 3, or q to quit: ")
        if choice == "q":
            return "q"
        if not choice.isdigit:
            print("Invalid input")
            continue
        num = int(choice)
        if choice.isdigit():
            if 1 <= num <= 3:
                continue
            else:
                print("Invalid input")
                continue
        if (num == 1 and rolled1) or (num ==2 and rolled2) or (num == 3 and rolled3):
            print("Sorry, you already rolled that dice. Try again.")
            continue
        
        return num


def roll_die():
    num = random.randit(DICE_MIN, DICE_MAX)
    return num

def show_state(d1, d2, d3, wins, losses):
    total = d1 + d2 + d3
    print(f"{d1} {d2} {d3} sum: {total} #win: {wins} #loss: {losses}")

def play_round(wins, losses):
    d1 = d2 = d3 = 0
    rolled1 = rolled2 = rolled3 = 0
    rolls_done = 0

    while rolls_done < 3:
        choice = read_choice(rolled1, rolled2, rolled3)
        if choice == "q":
            return "quit", wins, losses

        if choice == 1:
            d1 = roll_die()
            rolled1 = 1
        elif choice == 2:
            d2 = roll_die()
            rolled2 = 1
        elif choice == 3:
            d3 = roll_die()
            rolled3 = 1

        rolls_done += 1

        if rolls_done == 3:
            total = d1 + d2 + d3
            if total == TARGET:
                wins += 1
                print("You won!")
            elif total > TARGET:
                losses += 1
                print("You lost!")
            else:
                print("You neither won nor lost the game.")
            show_state(d1, d2, d3, wins, losses)
        else:
            show_state(d1, d2, d3, wins, losses)

    return "continue", wins, losses
            
       
            
def main():
    print_welcome()

    wins = 0
    losses = 0

    while True:
        result = play_round(wins, losses)
        if result == "quit":
            print(f"#win: {wins} #loss: {losses}")
            print("Game Over!")
            break
        elif result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        print("Next round!")
    print(f"#win: {wins} #loss: {losses}")
    print("Game Over!")
    
    d1 = d2 = d3 = 0
    wins = losses = 0

    rolled1 = rolled2 = rolled3 = 0

    rolls_done = 0
    while rolls_done < 3:
        choice = read_choice(rolled1, rolled2, rolled3)

        if choice == "q":
            print("#win:", wins, "#loss", losses)
            print("Game Over!")
            return

        if choice == 1:
            d1 = roll_die()
            rolled1 = 1
        elif choice == 2:
            d2 = roll_die()
            rolled2 = 1
        elif choice == 3:
            d3 = roll_die()
            rolled3 = 1

        rolls_done += 1
        show_state(d1, d2, d3, wins, losses)

    print("Round complete.")

    for num in range(3):
        choice = read_choice()
        if choice == "q":
            print("#win:", wins, "#loss:", losses)
            print("Game Over!")
        return


    


if __name__ == "__main__":
    main()
