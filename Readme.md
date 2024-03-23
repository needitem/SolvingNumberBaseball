# Minigame Solver GUI

This Python script creates a graphical user interface (GUI) to solve a minigame where the user needs to guess a 4-digit number with unique digits. The game provides feedback in the form of "balls" (digits in the correct number but in the wrong position) and "strikes" (digits in the correct number and in the correct position).

## Features

- GUI built with the Tkinter library
- Generate all possible 4-digit numbers with unique digits
- Make an initial random guess
- Filter the remaining possible numbers based on user input (balls and strikes)
- Display the next guess or the solution if found

## Usage

1. Run the script to open the GUI window.
2. The initial guess will be displayed in the "Guess" label.
3. Enter the number of "Balls" and "Strikes" for the current guess in the respective entry fields.
4. Click the "Guess" button to make the next guess.
5. Repeat steps 3 and 4 until the solution is found.
6. The solution will be displayed in a message box if found.

## Functions

- `__init__(self, master)`: Initializes the GUI components and the list of possible numbers.
- `make_guess(self, first_guess=False)`: Handles the guessing process, either making a random initial guess or filtering the remaining numbers based on user input.
- `generate_possible_numbers()`: Generates a list of all possible 4-digit numbers with unique digits.
- `filter_possible_numbers(possible_numbers, guess, balls, strikes)`: Filters the list of possible numbers based on the current guess and the provided balls and strikes.
- `make_guess(possible_numbers)`: Selects a random number from the list of possible numbers.

## Dependencies

- Python 3.x
- Tkinter (usually included in Python installations)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
