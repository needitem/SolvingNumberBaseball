import random

def generate_possible_numbers():
    possible_numbers = []
    for i in range(10000):
        number_str = str(i).zfill(4)  # Pad zeros to make it 4 digits
        if len(set(number_str)) == 4:  # Ensure all digits are unique
            possible_numbers.append(number_str)
    return possible_numbers

def filter_possible_numbers(possible_numbers, guess, balls, strikes):
    remaining_numbers = []
    for number in possible_numbers:
        temp_balls = 0
        temp_strikes = 0
        for i in range(4):
            if number[i] == guess[i]:
                temp_strikes += 1
            elif number[i] in guess:
                temp_balls += 1
        if temp_balls == balls and temp_strikes == strikes:
            remaining_numbers.append(number)
    return remaining_numbers

def make_guess(possible_numbers):
    return random.choice(possible_numbers)

def main():
    possible_numbers = generate_possible_numbers()
    while len(possible_numbers) > 1:
        guess = make_guess(possible_numbers)
        print("Guess:", guess)
        balls = int(input("Balls: "))
        strikes = int(input("Strikes: "))
        possible_numbers = filter_possible_numbers(possible_numbers, guess, balls, strikes)
    
    if len(possible_numbers) == 1:
        print("The number you called is:", possible_numbers[0])
    else:
        print("No valid number found.")

if __name__ == "__main__":
    main()
