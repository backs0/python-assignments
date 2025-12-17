import random

# --- Constants ---
MIN_RANDOM = 0
MAX_RANDOM = 999
INVALID_INPUT_MESSAGE = "Invalid Input"



def main():
    while True:
        num = input(f"How many random numbers in the range {MIN_RANDOM} – {MAX_RANDOM} are desired? ")
        try:
            num = int(num)
            if num < MIN_RANDOM:
                print(INVALID_INPUT_MESSAGE)
                break
            elif num > MAX_RANDOM:
                print (INVALID_INPUT_MESSAGE)
                break
        except ValueError:
            print(INVALID_INPUT_MESSAGE)
            break

        numbers = []
        while len(numbers) < num:
            try:
                i = random.randint(MIN_RANDOM, MAX_RANDOM)
                numbers.append(i)
            except MemoryError:
                print("Impossible to handle the requested amount of numbers on this system.")
                break

        print("\nHere are the random numbers: ")
        for x in numbers:
            print(x, end = " ")
        print()

        evens = []
        odds = []
        for x in numbers:
            if x % 2 == 0:
                evens.append(x)
            else:
                odds.append(x)

        def bubble_sort(numbers):
            n = len(numbers)
            for i in range(0, n):
                for j in range(0, n - i - 1):
                    if numbers[j] > numbers[j + 1]:
                        temp = numbers[j]
                        numbers[j] = numbers[j + 1]
                        numbers[j + 1] = temp

        def evens_list(numbers):
            numbers = evens[:]
            bubble_sort(numbers)
            numbers_even = numbers
            return numbers_even

        def odds_list(numbers):
            numbers = odds[:]
            bubble_sort(numbers)
            numbers_odd = numbers[::-1]
            return numbers_odd

        evens = evens_list(numbers)
        odds = odds_list(numbers)

        print("\nHere are the random numbers arranged: ")
        for num in evens:
            print(num, end = " ")
        if evens is None:
            print("No Even Numbers")

        for num in odds:
            print(num, end = " ")
        if odds =
            print("No Odd Numbers")

        break







# Run the program
if __name__ == "__main__":
    main()
